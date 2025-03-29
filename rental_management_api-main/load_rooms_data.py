import pandas as pd
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Room, Base

# Đảm bảo bảng được tạo trước khi nhập dữ liệu
Base.metadata.create_all(engine)

# Đọc dữ liệu từ file CSV
df = pd.read_csv("rooms.csv")

# Đổi tên cột trong DataFrame để khớp với database
df.rename(columns={
    "room_name": "name",
    "address": "address",
    "price": "price",
    "area": "area",
    "nearby_facilities": "nearby_facilities"
}, inplace=True)

# Kiểm tra xem tên cột đã đúng chưa
print(df.head())  # In ra 5 dòng đầu để kiểm tra dữ liệu

# Mở session
db = SessionLocal()

try:
    for _, row in df.iterrows():
        room = Room(
            name=row["name"],  # Trước đây là "room_name", giờ đã đổi thành "name"
            address=row["address"],
            price=row["price"],
            area=row["area"],
            nearby_facilities=row["nearby_facilities"]
        )
        db.add(room)

    db.commit()
    print("Dữ liệu đã được nhập thành công!")

except Exception as e:
    db.rollback()
    print(f"Đã xảy ra lỗi: {e}")

finally:
    db.close()
