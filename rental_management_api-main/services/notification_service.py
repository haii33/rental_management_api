import requests
from utils.logger import log_info
from models import Notification

def send_email_notification(user_id: int, message: str):
    email_api_url = "https://api.emailservice.com/send"
    response = requests.post(email_api_url, json={
        "user_id": user_id,
        "message": message
    })
    log_info(f"Email notification sent to user {user_id}: {message}")
    return response.json()

def send_sms_notification(user_id: int, message: str):
    sms_api_url = "https://api.smsservice.com/send"
    response = requests.post(sms_api_url, json={
        "user_id": user_id,
        "message": message
    })
    log_info(f"SMS notification sent to user {user_id}: {message}")
    return response.json()
