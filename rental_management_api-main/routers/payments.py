
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import PaymentSchema
from models import Payment
from database import get_db

router = APIRouter(prefix="/payments", tags=["Payments"])

@router.post("/")
async def make_payment(payment_data: PaymentSchema, db: Session = Depends(get_db)):
    new_payment = Payment(**payment_data.dict())
    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)
    
    return {"message": "Payment successful", "payment": new_payment}
