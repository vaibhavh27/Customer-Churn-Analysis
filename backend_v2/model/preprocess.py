
import numpy as np, pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

CATEGORICAL_COLS = [
    "gender","SeniorCitizen","Partner","Dependents","PhoneService","MultipleLines",
    "InternetService","OnlineSecurity","OnlineBackup","DeviceProtection","TechSupport",
    "StreamingTV","StreamingMovies","Contract","PaperlessBilling","PaymentMethod"
]
NUMERIC_COLS = ["tenure", "MonthlyCharges", "TotalCharges"]

def clean_telco(df: pd.DataFrame) -> pd.DataFrame:
    if "TotalCharges" in df.columns:
        df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    if "SeniorCitizen" in df.columns:
        df["SeniorCitizen"] = pd.to_numeric(df["SeniorCitizen"], errors="coerce").fillna(0).astype(int)
    for c in CATEGORICAL_COLS:
        if c in df.columns:
            df[c] = df[c].fillna("Unknown").astype(str)
    for c in NUMERIC_COLS:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce").fillna(df[c].median())
    return df

def build_preprocessor():
    return ColumnTransformer([
        ("cat", OneHotEncoder(handle_unknown="ignore"), CATEGORICAL_COLS),
        ("num", "passthrough", NUMERIC_COLS),
    ])

def feature_names_from(ct: ColumnTransformer):
    cat_names = []
    num_names = NUMERIC_COLS
    for name, trans, cols in ct.transformers_:
        if name == "cat":
            enc = trans
            if hasattr(enc, "get_feature_names_out"):
                cat_names = enc.get_feature_names_out(cols).tolist()
            else:
                cat_names = enc.get_feature_names(cols)
    return list(cat_names) + list(num_names)
