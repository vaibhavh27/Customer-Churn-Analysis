
import numpy as np
try:
    import shap
    SHAP_AVAILABLE = True
except Exception:
    SHAP_AVAILABLE = False

def top_reasons(model, x_row: np.ndarray, feature_names, k: int = 5):
    if SHAP_AVAILABLE:
        try:
            explainer = shap.Explainer(model, feature_names=feature_names)
            sv = explainer(x_row.reshape(1, -1)).values[0]
            order = np.argsort(np.abs(sv))[::-1][:k]
            return [{
                "feature": feature_names[i],
                "impact": float(sv[i]),
                "direction": "increase" if sv[i]>0 else "decrease"
            } for i in order]
        except Exception:
            pass
    if hasattr(model, "coef_"):
        coefs = model.coef_.ravel()
        contrib = x_row * coefs
    elif hasattr(model, "feature_importances_"):
        coefs = getattr(model, "feature_importances_")
        contrib = x_row * coefs
    else:
        contrib = x_row
    order = np.argsort(np.abs(contrib))[::-1][:k]
    return [{
        "feature": feature_names[i],
        "impact": float(contrib[i]),
        "direction": "increase" if contrib[i]>0 else "decrease"
    } for i in order]
