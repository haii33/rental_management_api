from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    full_name: str
    email: str
    phone_number: str
    identity_card: str
    password: str
    role: str  # "tenant" hoặc "owner"

class UserLogin(BaseModel):
    email: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str

class RoomCreate(BaseModel):
    number: str
    area: float
    price: float

class PaymentCreate(BaseModel):
    tenant_id: int
    room_id: int
    amount: float
    status: Optional[str] = "pending"

class RoomCreate(BaseModel):
    number: str
    area: float
    price: float
    status: Optional[str] = "available"

class UserUpdate(BaseModel):
    full_name: Optional[str]
    phone_number: Optional[str]
    email: Optional[str]
    identity_card: Optional[str]

class UserResponse(BaseModel):
    id: int
    full_name: str
    email: str
    phone_number: str
    identity_card: str
    role: str

    class Config:
        from_attributes = True