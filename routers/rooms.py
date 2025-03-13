from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Room
from schemas import RoomCreate
from typing import List

router = APIRouter(prefix="/rooms", tags=["Room Management"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 1️⃣ Thêm phòng mới
@router.post("/", response_model=RoomCreate)
def create_room(room: RoomCreate, db: Session = Depends(get_db)):
    db_room = Room(**room.dict())
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room

# 2️⃣ Lấy danh sách phòng
@router.get("/", response_model=List[RoomCreate])
def get_rooms(db: Session = Depends(get_db)):
    return db.query(Room).all()

# 3️⃣ Lọc phòng theo trạng thái, giá, diện tích
@router.get("/filter/")
def filter_rooms(status: str = None, min_price: float = 0, max_price: float = 9999999, db: Session = Depends(get_db)):
    query = db.query(Room)
    if status:
        query = query.filter(Room.status == status)
    query = query.filter(Room.price >= min_price, Room.price <= max_price)
    return query.all()

# 4️⃣ Cập nhật thông tin phòng
@router.put("/{room_id}")
def update_room(room_id: int, room: RoomCreate, db: Session = Depends(get_db)):
    db_room = db.query(Room).filter(Room.id == room_id).first()
    if not db_room:
        raise HTTPException(status_code=404, detail="Room not found")
    for key, value in room.dict().items():
        setattr(db_room, key, value)
    db.commit()
    return {"message": "Room updated successfully"}

# 5️⃣ Xóa phòng
@router.delete("/{room_id}")
def delete_room(room_id: int, db: Session = Depends(get_db)):
    db_room = db.query(Room).filter(Room.id == room_id).first()
    if not db_room:
        raise HTTPException(status_code=404, detail="Room not found")
    db.delete(db_room)
    db.commit()
    return {"message": "Room deleted successfully"}