from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import FinanceCreate, FinanceSchema
from models import Finance
from database import get_db

router = APIRouter(prefix="/finance", tags=["Finance"])

@router.get("/", response_model=list[FinanceSchema])
async def get_finance(db: Session = Depends(get_db)):
    return db.query(Finance).all()

@router.post("/", response_model=FinanceSchema)
async def create_finance(finance_data: FinanceCreate, db: Session = Depends(get_db)):
    new_finance = Finance(**finance_data.dict())
    db.add(new_finance)
    db.commit()
    db.refresh(new_finance)
    return new_finance

@router.put("/{finance_id}", response_model=FinanceSchema)
async def update_finance(finance_id: int, finance_data: FinanceCreate, db: Session = Depends(get_db)):
    finance = db.query(Finance).filter(Finance.id == finance_id).first()
    if not finance:
        raise HTTPException(status_code=404, detail="Finance record not found")
    for key, value in finance_data.dict(exclude_unset=True).items():
        setattr(finance, key, value)
    db.commit()
    db.refresh(finance)
    return finance

@router.delete("/{finance_id}")
async def delete_finance(finance_id: int, db: Session = Depends(get_db)):
    finance = db.query(Finance).filter(Finance.id == finance_id).first()
    if not finance:
        raise HTTPException(status_code=404, detail="Finance record not found")
    db.delete(finance)
    db.commit()
    return {"detail": "Finance record deleted successfully"}

@router.get("/stats")
async def get_finance_stats(db: Session = Depends(get_db)):
    total_income = db.query(Finance).filter(Finance.type == "income").sum(Finance.amount)
    total_expense = db.query(Finance).filter(Finance.type == "expense").sum(Finance.amount)
    return {"total_income": total_income, "total_expense": total_expense}
