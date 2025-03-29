from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import UserCreate, UserSchema, OrgCreate
from models import User, Organization
from utils.security import hash_password, create_access_token, verify_password
from database import get_db

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=UserSchema)
async def register(user_data: UserCreate, db: Session = Depends(get_db)):
    user_data.hashed_password = hash_password(user_data.password)
    new_user = User(**user_data.dict(exclude={"password"}))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/register-org", response_model=UserSchema)
async def register_org(org_data: OrgCreate, db: Session = Depends(get_db)):
    org_data.hashed_password = hash_password(org_data.password)
    new_org = Organization(**org_data.dict(exclude={"password"}))
    db.add(new_org)
    db.commit()
    db.refresh(new_org)
    return new_org

@router.post("/login")
async def login(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/profile", response_model=UserSchema)
async def get_profile(user: User = Depends(get_db)):
    return user

@router.put("/profile/update", response_model=UserSchema)
async def update_profile(user_data: UserCreate, db: Session = Depends(get_db), user: User = Depends(get_db)):
    for key, value in user_data.dict(exclude_unset=True).items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user

@router.put("/profile/password")
async def change_password(old_password: str, new_password: str, db: Session = Depends(get_db), user: User = Depends(get_db)):
    if not verify_password(old_password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect old password")
    user.hashed_password = hash_password(new_password)
    db.commit()
    return {"detail": "Password updated successfully"}
