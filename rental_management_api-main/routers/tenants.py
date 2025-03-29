from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User
from schemas import UserCreate  # Đảm bảo file schemas.py định nghĩa đúng UserCreate

router = APIRouter(prefix="/tenants", tags=["Tenant Management"])

# Dependency: Kết nối database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# API lấy danh sách khách thuê
@router.get("/")
def get_tenants(db: Session = Depends(get_db)):
    tenants = db.query(User).filter(User.role == "tenant").all()
    return {"tenants": tenants}

# API thêm khách thuê mới
@router.post("/")
def create_tenant(tenant: UserCreate, db: Session = Depends(get_db)):
    existing_tenant = db.query(User).filter(User.email == tenant.email).first()
    if existing_tenant:
        raise HTTPException(status_code=400, detail="Email đã tồn tại!")

    db_tenant = User(
        full_name=tenant.full_name,
        email=tenant.email,
        phone_number=tenant.phone_number,
        identity_card=tenant.identity_card,
        password_hash=tenant.password,  # Hãy đảm bảo mật khẩu đã được hash
        role="tenant"
    )
    db.add(db_tenant)
    db.commit()
    db.refresh(db_tenant)
    return {"message": "Thêm khách thuê thành công!", "tenant_id": db_tenant.id}

# API cập nhật thông tin khách thuê
@router.put("/{tenant_id}")
def update_tenant(tenant_id: int, tenant: UserCreate, db: Session = Depends(get_db)):
    db_tenant = db.query(User).filter(User.id == tenant_id, User.role == "tenant").first()
    if not db_tenant:
        raise HTTPException(status_code=404, detail="Không tìm thấy khách thuê!")

    db_tenant.full_name = tenant.full_name
    db_tenant.email = tenant.email
    db_tenant.phone_number = tenant.phone_number
    db_tenant.identity_card = tenant.identity_card
    db.commit()
    db.refresh(db_tenant)
    return {"message": "Cập nhật khách thuê thành công!", "tenant_id": db_tenant.id}

# API xóa khách thuê
@router.delete("/{tenant_id}")
def delete_tenant(tenant_id: int, db: Session = Depends(get_db)):
    db_tenant = db.query(User).filter(User.id == tenant_id, User.role == "tenant").first()
    if not db_tenant:
        raise HTTPException(status_code=404, detail="Không tìm thấy khách thuê!")

    db.delete(db_tenant)
    db.commit()
    return {"message": "Xóa khách thuê thành công!"}
