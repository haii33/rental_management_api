from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from database import Base, engine
import datetime

Base.metadata.create_all(bind=engine)

print("Database tables created successfully.")

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone_number = Column(String, unique=True, nullable=False)
    identity_card = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, nullable=False)
  
    payments = relationship("Payment", back_populates="user")
    notifications = relationship("Notification", back_populates="user")
  
class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)  # Đảm bảo đúng tên "name"
    address = Column(String(255), nullable=False)
    price = Column(Integer, nullable=False)
    area = Column(Float, nullable=False)
    nearby_facilities = Column(String(255), nullable=True)
  
class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(Integer, ForeignKey("users.id"))
    amount = Column(Float, nullable=False)
    payment_method = Column(String, nullable=False)
    payment_date = Column(DateTime, default=lambda: datetime.datetime.utcnow())
      
    user = relationship("User", back_populates="payments")
  
class Notification(Base):
    __tablename__ = "notifications"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    message = Column(String, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.datetime.utcnow())
    read = Column(Boolean, default=False)
      
    user = relationship("User", back_populates="notifications")
