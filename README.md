Customer Churn Prediction
Customer Churn Prediction is a modern web application for analyzing and predicting customer churn using machine learning on realistic business data. It features a Python FastAPI backend, JWT authentication, explainable churn risk, and a responsive web frontend for both single customers and batch CSV uploads.

UI Screenshots
Below are screenshots showing the application's user interface and workflows:

1. Login Page
<img src="./assets/login.png" alt="Login Page" width="700"/>
Overview: Secure login for authorized access, with demo credentials for testing.

Design: Clean, dark-themed layout; instant error feedback on login.

2. Prediction Dashboard
<img src="./assets/dashboard.png" alt="Prediction Dashboard" width="700"/>
Single Customer Prediction: Enter customer details to receive churn probability, risk score, influencing features, and retention recommendations.

Batch Prediction: Upload CSV files for batch churn prediction.

Global Insights: Access feature importance and business intelligence.

Responsive Layout: Adapts for desktop and laptop screens.

Features
Real Dataset Integration: Uses the IBM Telco Customer Churn dataset.

Machine Learning Model: XGBoost (if available) or Logistic Regression for accurate prediction.

Secure API Backend: FastAPI service, JWT login, protected endpoints.

Single & Batch Prediction: Predict for individuals and bulk CSVs in the web UI.

Explainable AI: Shows driving features and actionable recommendations for churn predictions.

Global Feature Insights: Top factors influencing churn across all customers.

Responsive Frontend: HTML, CSS, JS frontend adapts to screen size.

Deploy Locally: Runs on Windows, macOS, or Linux systems.

Tech Stack
Backend:

Python 3.8+

FastAPI, Uvicorn

Pandas, NumPy, scikit-learn, XGBoost (optional)

JWT via python-jose

passlib

Frontend:

HTML5, CSS3, JavaScript

Data:

IBM Telco Customer Churn dataset (auto-downloaded to data/ on training)

Prerequisites
Python 3.8+

pip

git

Modern browser (Chrome, Firefox, Edge, Safari)

Setup and Installation
Clone the Repository:

bash
git clone https://github.com/vaibhavh27/Customer-Churn-Analysis.git
cd Customer-Churn-Analysis
Create & Activate a Virtual Environment:

bash
python -m venv .venv
# Windows:
.\.venv\Scripts\Activate.ps1
# macOS/Linux:
source .venv/bin/activate
Install Dependencies:

bash
pip install -r requirements.txt
Train the Model:

bash
python -m backend/model/train
Downloads dataset, trains ML model, saves artifacts in backend's artifacts folder.

Start the Backend API:

bash
python -m uvicorn backend.app:app --reload
The API runs at http://127.0.0.1:8000/

Serve the Frontend:

bash
cd frontend
python -m http.server 5500 --bind 127.0.0.1
# Then go to: http://127.0.0.1:5500/index.html
Project Structure
text
Customer-Churn-Analysis/
├── backend/
│   ├── app.py
│   ├── model/
│   │   ├── train.py
│   │   ├── preprocess.py
│   │   ├── reason.py
│   │   ├── recommend.py
│   │   └── artifacts/
│   │       ├── model.pkl
│   │       ├── preprocessor.pkl
│   │       └── columns.json
│   ├── auth.py
│   ├── settings.py
├── data/
│   └── telco_customer_churn.csv
├── frontend/
│   ├── index.html
│   ├── app.js
│   └── styles.css
├── assets/
│   ├── login.png
│   └── dashboard.png
├── requirements.txt
└── README.md
API Endpoints
POST /auth/login — Authenticate and get JWT.

POST /predict — Predict churn for a single customer.

POST /predict_batch — Upload CSV, get batch churn predictions.

GET /insights — Global feature importance.

Troubleshooting
Back-end not running? Ensure model is trained and dependencies installed.

Login errors? Use correct credentials (admin / admin123), ensure API is running.

CSV issues? Make sure your file matches IBM dataset columns and structure.

Future Enhancements
Full mobile compatibility

Interactive charts for insights

Downloadable PDF/CSV reports

User registration and dashboards

Multi-model & hyperparameter selection in UI

License
MIT License. Free for academic, research, and commercial use.

Credits
Developed by Vaibhav Hingnekar
Dataset: IBM Telco Customer Churn

Explore churn analytics and actionable business intelligence on real-world customer data in seconds!
