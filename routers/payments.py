from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Payment
from schemas import PaymentCreate
from typing import List

router = APIRouter(prefix="/payments", tags=["Payment Management"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 1️⃣ Tạo thanh toán mới
@router.post("/", response_model=PaymentCreate)
def create_payment(payment: PaymentCreate, db: Session = Depends(get_db)):
    db_payment = Payment(**payment.dict())
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment

# 2️⃣ Lấy danh sách thanh toán
@router.get("/", response_model=List[PaymentCreate])
def get_payments(db: Session = Depends(get_db)):
    return db.query(Payment).all()

# 3️⃣ Cập nhật trạng thái thanh toán
@router.put("/{payment_id}")
def update_payment(payment_id: int, status: str, db: Session = Depends(get_db)):
    db_payment = db.query(Payment).filter(Payment.id == payment_id).first()
    if not db_payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    db_payment.status = status
    db.commit()
    return {"message": "Payment status updated successfully"}

# 4️⃣ Xóa giao dịch thanh toán
@router.delete("/{payment_id}")
def delete_payment(payment_id: int, db: Session = Depends(get_db)):
    db_payment = db.query(Payment).filter(Payment.id == payment_id).first()
    if not db_payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    db.delete(db_payment)
    db.commit()
    return {"message": "Payment deleted successfully"}