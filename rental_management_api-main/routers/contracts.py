from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import ContractCreate, ContractSchema
from models import Contract
from database import get_db

router = APIRouter(prefix="/contracts", tags=["Contracts"])

@router.get("/", response_model=list[ContractSchema])
async def get_contracts(db: Session = Depends(get_db)):
    return db.query(Contract).all()

@router.post("/", response_model=ContractSchema)
async def create_contract(contract_data: ContractCreate, db: Session = Depends(get_db)):
    new_contract = Contract(**contract_data.dict())
    db.add(new_contract)
    db.commit()
    db.refresh(new_contract)
    return new_contract

@router.put("/{contract_id}", response_model=ContractSchema)
async def update_contract(contract_id: int, contract_data: ContractCreate, db: Session = Depends(get_db)):
    contract = db.query(Contract).filter(Contract.id == contract_id).first()
    if not contract:
        raise HTTPException(status_code=404, detail="Contract not found")
    for key, value in contract_data.dict(exclude_unset=True).items():
        setattr(contract, key, value)
    db.commit()
    db.refresh(contract)
    return contract

@router.delete("/{contract_id}")
async def delete_contract(contract_id: int, db: Session = Depends(get_db)):
    contract = db.query(Contract).filter(Contract.id == contract_id).first()
    if not contract:
        raise HTTPException(status_code=404, detail="Contract not found")
    db.delete(contract)
    db.commit()
    return {"detail": "Contract deleted successfully"}

@router.post("/{contract_id}/cancel")
async def cancel_contract(contract_id: int, db: Session = Depends(get_db)):
    contract = db.query(Contract).filter(Contract.id == contract_id).first()
    if not contract:
        raise HTTPException(status_code=404, detail="Contract not found")
    contract.status = "Cancelled"
    db.commit()
    return {"detail": "Contract cancelled successfully"}

@router.get("/me", response_model=list[ContractSchema])
async def get_my_contracts(db: Session = Depends(get_db)):
    return db.query(Contract).filter(Contract.user_id == 1).all()  # Thay 1 bằng user_id từ auth
