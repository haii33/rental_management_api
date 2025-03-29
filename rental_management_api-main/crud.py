from sqlalchemy.orm import Session
from models import User, Room, Payment
from schemas import UserCreate, RoomCreate, PaymentCreate

# Xử lý User
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, user: UserCreate):
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Xử lý Room
def get_rooms(db: Session):
    return db.query(Room).all()

def create_room(db: Session, room: RoomCreate):
    db_room = Room(**room.model_dump())
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room

# Xử lý Payment
def get_payments(db: Session):
    return db.query(Payment).all()