from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User, Payment
from schemas import UserUpdate, UserResponse
from typing import List
from fastapi.security import OAuth2PasswordBearer

router = APIRouter(prefix="/profile", tags=["User Profile"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 1️⃣ Xem thông tin cá nhân
@router.get("/", response_model=UserResponse)
def get_profile(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# 2️⃣ Cập nhật thông tin cá nhân
@router.put("/")
def update_profile(user_id: int, user_data: UserUpdate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    for key, value in user_data.dict(exclude_unset=True).items():
        setattr(user, key, value)

    db.commit()
    return {"message": "User profile updated successfully"}

# 3️⃣ Lấy lịch sử giao dịch của người dùng
@router.get("/transactions", response_model=List[dict])
def get_user_transactions(user_id: int, db: Session = Depends(get_db)):
    transactions = db.query(Payment).filter(Payment.tenant_id == user_id).all()
    if not transactions:
        raise HTTPException(status_code=404, detail="No transactions found")
    
    return [{"id": t.id, "room_id": t.room_id, "amount": t.amount, "status": t.status, "created_at": t.created_at} for t in transactions]