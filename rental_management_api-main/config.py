import os
from dotenv import load_dotenv

# Load biến môi trường từ file .env
load_dotenv()

# Cấu hình database
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./rental_management.db")

# Cấu hình JWT
SECRET_KEY = os.getenv("JWT_SECRET", "your_jwt_secret_key")

# Cấu hình logging
LOG_FILE = os.getenv("LOG_FILE", "logs/app.log")

SQLALCHEMY_DATABASE_URI = "sqlite:///rental_management.db"
