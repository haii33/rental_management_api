from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User
from schemas import UserUpdate
from utils.security import get_current_user

router = APIRouter(prefix="/profile", tags=["User Profile"])

# Dependency: Kết nối database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# API lấy thông tin cá nhân
@router.get("/")
def get_profile(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return {"user_id": current_user.id, "full_name": current_user.full_name, "email": current_user.email, "phone_number": current_user.phone_number, "identity_card": current_user.identity_card}

# API cập nhật thông tin cá nhân
@router.put("/")
def update_profile(user_update: UserUpdate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == current_user.id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Không tìm thấy người dùng!")

    db_user.full_name = user_update.full_name
    db_user.phone_number = user_update.phone_number
    db.commit()
    db.refresh(db_user)
    return {"message": "Cập nhật thông tin cá nhân thành công!"}
