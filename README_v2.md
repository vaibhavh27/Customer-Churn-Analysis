
# Customer Churn Prediction v2 (Real Dataset + Login + Better UI)

**New project** (does not edit the old one).

## Layout
- `backend_v2/` — FastAPI app with JWT auth (`backend_v2/app_v2.py`)
- `backend_v2/model/train_v2.py` — trains on IBM Telco Customer Churn (auto-download)
- `frontend_v2/` — login + improved UI
- `data_v2/` — dataset folder
- `requirements_v2.txt` — dependencies

## Run (Windows PowerShell)
```powershell
cd churn_project_v2
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements_v2.txt

# Train (downloads real dataset)
python -m backend_v2.model.train_v2

# Start API
python -m uvicorn backend_v2.app_v2:app --reload

# Frontend (new terminal)
cd frontend_v2
python -m http.server 5500 --bind 127.0.0.1
# open http://127.0.0.1:5500/index.html
```
Login in the UI with **admin / admin123** (or set `CHURN_V2_USER` / `CHURN_V2_PASS`).
