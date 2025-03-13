from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User
from schemas import UserCreate
from typing import List

router = APIRouter(prefix="/tenants", tags=["Tenant Management"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 1️⃣ Thêm khách thuê
@router.post("/", response_model=UserCreate)
def create_tenant(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# 2️⃣ Lấy danh sách khách thuê
@router.get("/", response_model=List[UserCreate])
def get_tenants(db: Session = Depends(get_db)):
    return db.query(User).filter(User.role == "tenant").all()

# 3️⃣ Cập nhật thông tin khách thuê
@router.put("/{tenant_id}")
def update_tenant(tenant_id: int, user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == tenant_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Tenant not found")
    for key, value in user.dict().items():
        setattr(db_user, key, value)
    db.commit()
    return {"message": "Tenant updated successfully"}

# 4️⃣ Xóa khách thuê
@router.delete("/{tenant_id}")
def delete_tenant(tenant_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == tenant_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Tenant not found")
    db.delete(db_user)
    db.commit()
    return {"message": "Tenant deleted successfully"}