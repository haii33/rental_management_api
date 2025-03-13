from fastapi import FastAPI
from database import engine, Base
from routers.auth import router as auth_router

app = FastAPI()

# Khởi tạo database
Base.metadata.create_all(bind=engine)

# Đăng ký router
app.include_router(auth_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Rental Management API!"}