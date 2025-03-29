from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Notification
from schemas import NotificationCreate
from services.notification_service import send_email_notification, send_sms_notification

router = APIRouter(prefix="/notifications", tags=["Notification Management"])

# Dependency: Kết nối database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# API lấy danh sách thông báo
@router.get("/")
def get_notifications(db: Session = Depends(get_db)):
    notifications = db.query(Notification).all()
    return {"notifications": notifications}

# API gửi thông báo qua email
@router.post("/email/")
def email_notification(notification: NotificationCreate, db: Session = Depends(get_db)):
    response = send_email_notification(notification.user_id, notification.message)
    return response

# API gửi thông báo qua SMS
@router.post("/sms/")
def sms_notification(notification: NotificationCreate, db: Session = Depends(get_db)):
    response = send_sms_notification(notification.user_id, notification.message)
    return response
