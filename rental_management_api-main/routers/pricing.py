from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import PricingSchema, SubscriptionCreate
from models import Pricing, Subscription
from database import get_db

router = APIRouter(prefix="/pricing", tags=["Pricing & Subscription"])

@router.get("/", response_model=list[PricingSchema])
async def get_pricing(db: Session = Depends(get_db)):
    return db.query(Pricing).all()

@router.post("/subscribe")
async def subscribe(subscription_data: SubscriptionCreate, db: Session = Depends(get_db)):
    new_subscription = Subscription(**subscription_data.dict())
    db.add(new_subscription)
    db.commit()
    db.refresh(new_subscription)
    return {"detail": "Subscription created successfully"}

@router.get("/subscription/status")
async def get_subscription_status(db: Session = Depends(get_db)):
    active_subscriptions = db.query(Subscription).filter(Subscription.status == "active").all()
    return {"active_subscriptions": active_subscriptions}
