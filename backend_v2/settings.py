
import os
SECRET_KEY = os.getenv("CHURN_V2_SECRET", "devsupersecretkey")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 8
DEMO_USER = os.getenv("CHURN_V2_USER", "admin")
DEMO_PASS = os.getenv("CHURN_V2_PASS", "admin123")
