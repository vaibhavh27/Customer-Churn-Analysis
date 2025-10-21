
import json, joblib, warnings, numpy as np, pandas as pd, os, urllib.request
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, classification_report
from sklearn.linear_model import LogisticRegression
try:
    from xgboost import XGBClassifier
    HAS_XGB = True
except Exception:
    HAS_XGB = False

from .preprocess import build_preprocessor, feature_names_from, clean_telco, CATEGORICAL_COLS, NUMERIC_COLS

ART_DIR = Path(__file__).parent / "artifacts"
ART_DIR.mkdir(parents=True, exist_ok=True)

TELCO_URLS = [
    "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv",
    "https://raw.githubusercontent.com/blastchar/telco-customer-churn/master/WA_Fn-UseC_-Telco-Customer-Churn.csv"
]

def download_telco_csv(dest: Path) -> Path:
    for url in TELCO_URLS:
        try:
            print("Trying:", url)
            data = urllib.request.urlopen(url, timeout=15).read()
            dest.write_bytes(data)
            print("Downloaded dataset to", dest)
            return dest
        except Exception as e:
            print("Warning: could not download from", url, "->", e)
    raise RuntimeError("Failed to download Telco dataset from all sources. Place a CSV manually at " + str(dest))

def load_telco_csv(data_dir: Path) -> pd.DataFrame:
    dest = data_dir / "telco_customer_churn.csv"
    if not dest.exists():
        download_telco_csv(dest)
    df = pd.read_csv(dest)
    if "Churn" not in df.columns:
        for c in df.columns:
            if c.lower() == "churn":
                df = df.rename(columns={c:"Churn"})
                break
    return df

def train(data_dir: str):
    data_dir = Path(data_dir)
    df = load_telco_csv(data_dir)
    df = clean_telco(df)
    y = (df["Churn"].astype(str).str.strip().str.lower() == "yes").astype(int).values
    X = df[CATEGORICAL_COLS + NUMERIC_COLS]
    preproc = build_preprocessor()
    X_enc = preproc.fit_transform(X)
    X_arr = X_enc.toarray() if hasattr(X_enc, "toarray") else np.asarray(X_enc)
    X_train, X_test, y_train, y_test = train_test_split(X_arr, y, test_size=0.2, random_state=42, stratify=y)

    if HAS_XGB:
        model = XGBClassifier(
            n_estimators=350, max_depth=4, learning_rate=0.08, subsample=0.9, colsample_bytree=0.9,
            reg_lambda=1.0, objective="binary:logistic", eval_metric="logloss", random_state=42
        )
    else:
        warnings.warn("XGBoost not found; using LogisticRegression fallback.")
        model = LogisticRegression(max_iter=400)

    model.fit(X_train, y_train)
    proba = model.predict_proba(X_test)[:,1]
    auc = roc_auc_score(y_test, proba)
    print(f"AUC: {auc:.3f}")
    print(classification_report(y_test, proba>=0.5))

    joblib.dump(model, ART_DIR / "model_v2.pkl")
    joblib.dump(preproc, ART_DIR / "preprocessor_v2.pkl")
    with open(ART_DIR / "columns_v2.json","w") as f:
        json.dump({"feature_names": feature_names_from(preproc)}, f, indent=2)
    return auc

if __name__ == "__main__":
    data_dir = Path(__file__).resolve().parents[2] / "data_v2"
    data_dir.mkdir(parents=True, exist_ok=True)
    train(str(data_dir))
