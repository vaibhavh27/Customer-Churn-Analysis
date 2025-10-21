# 🔮 Customer Churn Prediction

A modern web application for analyzing and predicting customer churn using machine learning on realistic business data. Features a Python FastAPI backend with JWT authentication, explainable AI for churn risk analysis, and a responsive web frontend supporting both single customer predictions and batch CSV uploads.

---

## 📸 UI Screenshots

### Login Page
<img src="./assets/login.png" alt="Login Page" width="700"/>

**Features:**
- Secure authentication for authorized access
- Demo credentials available for testing
- Clean, dark-themed design with instant error feedback

### Prediction Dashboard
<img src="./assets/dashboard.png" alt="Prediction Dashboard" width="700"/>

**Capabilities:**
- **Single Customer Prediction** - Enter customer details to receive churn probability, risk score, influencing features, and retention recommendations
- **Batch Prediction** - Upload CSV files for bulk churn prediction
- **Global Insights** - Access feature importance and business intelligence
- **Responsive Layout** - Adapts seamlessly to desktop and laptop screens

---

## ✨ Features

- **Real Dataset Integration** - Uses the IBM Telco Customer Churn dataset
- **Machine Learning Model** - XGBoost (if available) or Logistic Regression for accurate predictions
- **Secure API Backend** - FastAPI service with JWT authentication and protected endpoints
- **Single & Batch Prediction** - Predict for individual customers or bulk CSVs through the web UI
- **Explainable AI** - Shows driving features and actionable recommendations for churn predictions
- **Global Feature Insights** - Analyze top factors influencing churn across all customers
- **Responsive Frontend** - Modern HTML, CSS, and JavaScript frontend that adapts to screen size
- **Easy Local Deployment** - Runs on Windows, macOS, or Linux systems

---

## 🛠️ Tech Stack

**Backend:**
- Python 3.8+
- FastAPI & Uvicorn
- Pandas, NumPy, scikit-learn
- XGBoost (optional)
- JWT authentication via python-jose
- passlib for password hashing

**Frontend:**
- HTML5, CSS3, JavaScript

**Data:**
- IBM Telco Customer Churn dataset (auto-downloaded during training)

---

## 📋 Prerequisites

- Python 3.8 or higher
- pip package manager
- git
- Modern web browser (Chrome, Firefox, Edge, or Safari)

---

## 🚀 Setup and Installation

### 1. Clone the Repository

```bash
git clone https://github.com/vaibhavh27/Customer-Churn-Analysis.git
cd Customer-Churn-Analysis
```

### 2. Create & Activate Virtual Environment

```bash
python -m venv .venv

# Windows:
.\.venv\Scripts\Activate.ps1

# macOS/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Train the Model

```bash
python -m backend.model.train
```

This will download the dataset, train the ML model, and save artifacts in the `backend/artifacts/` folder.

### 5. Start the Backend API

```bash
python -m uvicorn backend.app:app --reload
```

The API will be available at `http://127.0.0.1:8000/`

### 6. Serve the Frontend

```bash
cd frontend
python -m http.server 5500 --bind 127.0.0.1
```

Then navigate to: `http://127.0.0.1:5500/index.html`

---

## 📁 Project Structure

```
Customer-Churn-Analysis/
│
├── backend/
│   ├── app.py                      # Main FastAPI application
│   ├── auth.py                     # JWT authentication
│   ├── settings.py                 # Configuration settings
│   │
│   └── model/
│       ├── train.py                # Model training script
│       ├── preprocess.py           # Data preprocessing
│       ├── reason.py               # Churn reason explanations
│       ├── recommend.py            # Retention recommendations
│       │
│       └── artifacts/
│           ├── model.pkl           # Trained model
│           ├── preprocessor.pkl    # Data preprocessor
│           └── columns.json        # Feature columns
│
├── data/
│   └── telco_customer_churn.csv    # Dataset
│
├── frontend/
│   ├── index.html                  # Main HTML page
│   ├── app.js                      # JavaScript logic
│   └── styles.css                  # Styling
│
├── assets/
│   ├── login.png                   # Login screenshot
│   └── dashboard.png               # Dashboard screenshot
│
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/auth/login` | Authenticate and receive JWT token |
| `POST` | `/predict` | Predict churn for a single customer |
| `POST` | `/predict_batch` | Upload CSV for batch churn predictions |
| `GET` | `/insights` | Get global feature importance |

---

## 🐛 Troubleshooting

**Backend not running?**
- Ensure the model is trained: `python -m backend.model.train`
- Verify all dependencies are installed: `pip install -r requirements.txt`

**Login errors?**
- Use the correct demo credentials: `admin` / `admin123`
- Confirm the backend API is running at `http://127.0.0.1:8000`

**CSV upload issues?**
- Ensure your CSV file matches the IBM dataset columns and structure
- Check that the file is properly formatted and contains no corrupted data

---

## 🚧 Future Enhancements

- [ ] Full mobile compatibility
- [ ] Interactive charts for insights visualization
- [ ] Downloadable PDF/CSV reports
- [ ] User registration and personalized dashboards
- [ ] Multi-model support with hyperparameter selection in UI
- [ ] Real-time prediction updates

---

## 📄 License

This project is licensed under the MIT License - free for academic, research, and commercial use.

---

## 👨‍💻 Credits

**Developed by:** [Vaibhav Hingnekar](https://github.com/vaibhavh27)

**Dataset:** [IBM Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

---

## 🎯 Getting Started

Explore churn analytics and actionable business intelligence on real-world customer data in seconds!

For questions or contributions, please open an issue or submit a pull request.

**Happy Predicting! 🚀**
