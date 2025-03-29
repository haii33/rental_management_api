import requests
from utils.logger import log_info

def process_bank_transfer(tenant_id: int, room_id: int, amount: float):
    bank_api_url = "https://api.bank.com/transfer"
    response = requests.post(bank_api_url, json={
        "tenant_id": tenant_id,
        "room_id": room_id,
        "amount": amount
    })
    log_info(f"Bank transfer requested for tenant {tenant_id}, amount {amount}")
    return response.json()

def process_zalopay_payment(tenant_id: int, amount: float):
    zalopay_api_url = "https://sandbox.zalopay.vn/v2/create"
    response = requests.post(zalopay_api_url, json={
        "app_id": "YOUR_ZALOPAY_APP_ID",
        "amount": amount,
        "description": f"Thanh toán hóa đơn từ tenant {tenant_id}",
        "callback_url": "https://yourdomain.com/callback",
        "tenant_id": tenant_id
    })
    log_info(f"ZaloPay payment requested for tenant {tenant_id}, amount {amount}")
    return response.json()
