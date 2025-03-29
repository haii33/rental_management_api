from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL kết nối đến cơ sở dữ liệu SQLite
DATABASE_URL = "sqlite:///database.db"  # Đảm bảo file này tồn tại
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Tạo engine kết nối cơ sở dữ liệu
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Hàm get_db để lấy session kết nối đến database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
