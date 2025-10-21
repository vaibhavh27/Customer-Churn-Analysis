💡 Customer Churn Prediction

A modern web application that helps businesses analyze and predict customer churn using machine learning algorithms and real-world data.

Built with a Python FastAPI backend, secure JWT authentication, and a responsive frontend for both single and batch predictions.

🚀 Features

Real Dataset Integration: Uses the IBM Telco Customer Churn dataset for realistic churn analysis.

Machine Learning Model: Trains and deploys XGBoost (or Logistic Regression) for accurate predictions.

Secure API Backend: Built with FastAPI + JWT authentication.

Single & Batch Prediction: Predict churn for one customer or upload a full CSV file.

Explainable AI: Shows key features driving each prediction and actionable insights.

Global Insights: Displays overall feature importance across all customers.

Responsive Frontend: HTML, CSS, and JavaScript frontend that works across devices.

Local Deployment: Easy to set up on Windows, macOS, or Linux.

🧠 Tech Stack

Backend:

Python 3.8+

FastAPI, Uvicorn

Pandas, NumPy, scikit-learn, XGBoost

python-jose (JWT), passlib

Frontend:

HTML5, CSS3, JavaScript (Vanilla)

Data:

IBM Telco Customer Churn dataset

📂 Project Structure
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
│   └── settings.py
├── data/
│   └── telco_customer_churn.csv
├── frontend/
│   ├── index.html
│   ├── app.js
│   └── styles.css
├── requirements.txt
└── README.md

⚙️ Setup & Installation
1️⃣ Clone the Repository
git clone https://github.com/vaibhavh27/Customer-Churn-Analysis.git
cd Customer-Churn-Analysis

2️⃣ Create and Activate a Virtual Environment
python -m venv .venv
# Windows
.\.venv\Scripts\Activate.ps1
# macOS/Linux
source .venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Train the Model
python -m backend.model.train


This script downloads the IBM Telco dataset, preprocesses data, trains the ML model, and saves artifacts inside backend/model/artifacts/.

5️⃣ Start the Backend API
python -m uvicorn backend.app:app --reload


Runs the API at: http://127.0.0.1:8000/

6️⃣ Serve the Frontend

Open a new terminal and run:

cd frontend
python -m http.server 5500 --bind 127.0.0.1


Then open http://127.0.0.1:5500/index.html
 in your browser.

🔑 API Endpoints
Method	Endpoint	Description
POST	/auth/login	Authenticate users and return JWT token
POST	/predict	Predict churn for a single customer
POST	/predict_batch	Upload CSV file for batch churn predictions
GET	/insights	Get global feature importance
🧾 Example Screenshots
🔐 Login Page

Secure login for authorized access.
Replace the paths below with correct ones from your repo.


📊 Prediction Dashboard

Predict churn for individual or multiple customers.


🧰 Troubleshooting

Backend not running?
Ensure the ML model is trained and dependencies are installed.

Login errors?
Use default credentials (admin / admin123) and confirm API is active.

CSV upload issues?
Verify your CSV columns match the IBM Telco dataset structure.

🔮 Future Enhancements

📱 Full mobile compatibility

📈 Interactive feature insight charts

📄 Downloadable PDF/CSV reports

👤 User registration and custom dashboards

⚙️ Multi-model and hyperparameter tuning support

🧑‍💻 Author

Developed by: Vaibhav Hingnekar

Dataset: IBM Telco Customer Churn

📜 License: MIT License — free for academic, research, and commercial use.
