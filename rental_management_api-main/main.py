from fastapi import FastAPI
from database import engine, Base
from routers import auth, rooms, tenants, payments, profile, notifications
from routers import chatbot

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(rooms.router)
app.include_router(tenants.router)
app.include_router(payments.router)
app.include_router(profile.router)
app.include_router(notifications.router)
app.include_router(chatbot.router, prefix="/chatbot", tags=["Chatbot"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Rental Management API!"}
