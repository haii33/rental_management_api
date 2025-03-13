from fastapi import FastAPI
from database import engine, Base
from routers.auth import router as auth_router
from routers import auth, rooms
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from routers import auth, rooms, tenants, payments, profile

app = FastAPI()

# Khởi tạo database
Base.metadata.create_all(bind=engine)

# Đăng ký router
app.include_router(auth_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Rental Management API!"}

app.include_router(auth.router)
app.include_router(rooms.router)
app.include_router(tenants.router)
app.include_router(payments.router)
app.include_router(profile.router)