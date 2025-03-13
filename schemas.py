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