from database import Base, engine

print("Khởi tạo database...")
Base.metadata.create_all(bind=engine)
print("Database đã sẵn sàng!")
