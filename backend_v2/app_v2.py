
import json, joblib, numpy as np, pandas as pd
from fastapi import FastAPI, UploadFile, File, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pathlib import Path
from typing import List
from .auth import create_access_token, verify_user, require_token
from .model.preprocess import CATEGORICAL_COLS, NUMERIC_COLS, build_preprocessor, feature_names_from, clean_telco
from .model.reason import top_reasons
from .model.recommend import recommend_actions

ART_DIR = Path(__file__).parent / "model" / "artifacts"

app = FastAPI(title="Churn Prediction API v2", version="2.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

class Login(BaseModel):
    username: str
    password: str

@app.post("/auth/login")
def login(payload: Login):
    if verify_user(payload.username, payload.password):
        token = create_access_token({"sub": payload.username})
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

def load_artifacts():
    model = joblib.load(ART_DIR / "model_v2.pkl")
    preproc = joblib.load(ART_DIR / "preprocessor_v2.pkl")
    with open(ART_DIR / "columns_v2.json","r") as f:
        feat_names = json.load(f)["feature_names"]
    return model, preproc, feat_names

@app.get("/ping")
def ping(): return {"status":"ok", "version":"v2"}

_loaded = {"model": None, "preproc": None, "feature_names": None}
def ensure_loaded():
    if _loaded["model"] is None:
        model, preproc, feature_names = load_artifacts()
        _loaded.update({"model": model, "preproc": preproc, "feature_names": feature_names})
    return _loaded["model"], _loaded["preproc"], _loaded["feature_names"]

@app.post("/predict")
def predict(row: dict, user = Depends(require_token)):
    model, preproc, feature_names = ensure_loaded()
    df = pd.DataFrame([row])
    df = clean_telco(df)
    required = [*CATEGORICAL_COLS, *NUMERIC_COLS]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise HTTPException(status_code=400, detail=f"Missing columns: {missing}")
    X = preproc.transform(df[required])
    X_arr = X.toarray() if hasattr(X, "toarray") else np.asarray(X)
    prob = float(model.predict_proba(X_arr)[0,1])
    reasons = top_reasons(model, X_arr[0], feature_names, k=5)
    actions = recommend_actions(reasons, top_k=3)
    risk = "High" if prob >= 0.65 else "Medium" if prob >= 0.4 else "Low"
    return {"churn_probability": prob, "risk": risk, "top_reasons": reasons, "recommendations": actions}

@app.post("/predict_batch")
async def predict_batch(file: UploadFile = File(...), user = Depends(require_token)):
    import io
    content = await file.read()
    df = pd.read_csv(io.StringIO(content.decode("utf-8")))
    df = clean_telco(df)
    required = [*CATEGORICAL_COLS, *NUMERIC_COLS, "Churn"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise HTTPException(status_code=400, detail=f"Missing columns: {missing}")
    model, preproc, feature_names = ensure_loaded()
    X = preproc.transform(df[[*CATEGORICAL_COLS, *NUMERIC_COLS]])
    X_arr = X.toarray() if hasattr(X,"toarray") else np.asarray(X)
    probs = model.predict_proba(X_arr)[:,1]
    risks = np.where(probs>=0.65,"High", np.where(probs>=0.4,"Medium","Low"))
    out = df.copy()
    out["predicted_churn_probability"] = probs
    out["predicted_risk"] = risks
    examples = []
    for i in range(min(3, len(out))):
        reasons = top_reasons(model, X_arr[i], feature_names, k=5)
        actions = recommend_actions(reasons, top_k=3)
        examples.append({"row_index": int(i), "churn_probability": float(probs[i]), "risk": str(risks[i]),
                         "top_reasons": reasons, "recommendations": actions})
    return {"summary_examples": examples, "preview_rows": out.head(50).to_dict(orient="records")}

@app.get("/insights")
def insights(user = Depends(require_token)):
    model, preproc, feature_names = ensure_loaded()
    if hasattr(model,"feature_importances_"):
        imps = model.feature_importances_
    elif hasattr(model,"coef_"):
        import numpy as np
        imps = np.abs(model.coef_.ravel())
    else:
        import numpy as np
        imps = np.ones(len(feature_names))
    pairs = sorted([{"feature":f,"importance":float(v)} for f,v in zip(feature_names, imps)],
                   key=lambda x: x["importance"], reverse=True)[:20]
    return {"top_features": pairs}
