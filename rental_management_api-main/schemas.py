from pydantic import BaseModel
from typing import Optional
import datetime

# Schema cho User
class UserBase(BaseModel):
    full_name: str
    email: str
    phone_number: str
    identity_card: str
    role: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True

# Schema cho Room
class RoomBase(BaseModel):
    number: str
    area: float
    price: float
    status: Optional[str] = "available"

class RoomCreate(RoomBase):
    pass

class RoomResponse(RoomBase):
    id: int

    class Config:
        from_attributes = True

# Schema cho Payment
class PaymentBase(BaseModel):
    tenant_id: int
    amount: float
    payment_method: str
    payment_date: Optional[datetime.datetime] = None

class PaymentCreate(PaymentBase):
    pass

class PaymentResponse(PaymentBase):
    id: int

    class Config:
        from_attributes = True

# Schema cho Notification
class NotificationBase(BaseModel):
    user_id: int
    message: str
    read: Optional[bool] = False

class NotificationCreate(NotificationBase):
    pass

class NotificationResponse(NotificationBase):
    id: int
    created_at: datetime.datetime

    class Config:
        from_attributes = True
