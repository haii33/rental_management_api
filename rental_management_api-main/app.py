import requests
import uuid
import hmac
import hashlib
import json
import urllib.parse
import qrcode
import time
from datetime import datetime

# Nhập số tiền và email từ người dùng
amount_str = input("Nhập số tiền muốn thanh toán: ").strip()
if not amount_str.isdigit() or int(amount_str) <= 0:
    print(" Số tiền không hợp lệ! Vui lòng nhập số nguyên dương.")
    exit()
amount = int(amount_str)

email = input("Nhập email của bạn: ").strip()

# Cấu hình API
MOMO_CONFIG = {
    "accessKey": "F8BBA842ECF85",
    "secretKey": "K951B6PE1waDMi640xX08PD3vg6EkVlz",
    "partnerCode": "MOMO",
    "endpoint": "https://test-payment.momo.vn/v2/gateway/api/create"
}

ZALOPAY_CONFIG = {
    "app_id": "2554",
    "key1": "sdngKKJmqEMzvh5QQcdD2A9XBSKUNaYn",
    "endpoint_create": "https://sb-openapi.zalopay.vn/v2/create"
}

BANK_ACCOUNT = "0123456789"
BANK_ID = "970422"  # Vietcombank

# Tạo link thanh toán MoMo
def get_momo_payment_link(amount):
    order_id = str(uuid.uuid4())
    request_id = str(uuid.uuid4())
    redirect_url = "https://webhook.site/test"

    raw_signature = f"accessKey={MOMO_CONFIG['accessKey']}&amount={amount}&extraData=&ipnUrl={redirect_url}&orderId={order_id}&orderInfo=Thanh toán MoMo&partnerCode={MOMO_CONFIG['partnerCode']}&redirectUrl={redirect_url}&requestId={request_id}&requestType=payWithMethod"
    signature = hmac.new(MOMO_CONFIG['secretKey'].encode(), raw_signature.encode(), hashlib.sha256).hexdigest()

    payload = {
        "partnerCode": MOMO_CONFIG['partnerCode'],
        "requestType": "payWithMethod",
        "ipnUrl": redirect_url,
        "redirectUrl": redirect_url,
        "orderId": order_id,
        "amount": amount,
        "orderInfo": "Thanh toán MoMo",
        "requestId": request_id,
        "extraData": "",
        "signature": signature
    }

    response = requests.post(MOMO_CONFIG["endpoint"], json=payload, headers={'Content-Type': 'application/json'})
    return response.json().get('payUrl', " Lỗi tạo link thanh toán MoMo!")

# Tạo đơn hàng ZaloPay
def create_zalopay_payment(amount, email):
    trans_id = str(int(time.time() * 1000))[-6:]
    app_trans_id = f"{datetime.now().strftime('%y%m%d')}_{trans_id}"
    app_time = int(time.time() * 1000)

    order = {
    "app_id": ZALOPAY_CONFIG["app_id"],
    "app_trans_id": app_trans_id,
    "app_user": email,
    "app_time": app_time,
    "amount": amount,
    "item": json.dumps([
        {"itemid": "rent_fee", "itemname": "Tiền thuê phòng", "itemprice": amount, "itemquantity": 1}
    ], ensure_ascii=False),
    "embed_data": json.dumps({"email": email}),
    "callback_url": "https://yourserver.com/callback",
    "description": "Thanh toán tiền thuê phòng",
    "bank_code": "zalopayapp"
}

#  Tạo chữ ký MAC
    # Kiểm tra chữ ký MAC
    raw_data = f"{ZALOPAY_CONFIG['app_id']}|{order['app_trans_id']}|{order['app_user']}|{order['amount']}|{order['app_time']}|{order['embed_data']}|{order['item']}"
    mac = hmac.new(ZALOPAY_CONFIG["key1"].encode(), raw_data.encode(), hashlib.sha256).hexdigest()
    order["mac"] = mac

#  Gửi request tạo thanh toán
    headers = {"Content-Type": "application/json"}
    response = requests.post(ZALOPAY_CONFIG["endpoint_create"], json=order, headers=headers)
    return response.json()
# Tạo mã QR VietQR
def generate_vietqr_web_link(bank_id, bank_account, amount, description):
    description_encoded = urllib.parse.quote(description)  # Mã hóa nội dung
    vietqr_web_link = f"https://vietqr.net/?amount={amount}&acc={bank_account}&bank={bank_id}&note={description_encoded}"
    return vietqr_web_link

# Định nghĩa thông tin ngân hàng
bank_id = "970422"  # Mã ngân hàng (Ví dụ: Vietcombank)
bank_account = "123456789"  # Số tài khoản ngân hàng

# Gọi hàm tạo link VietQR
bank_qr = generate_vietqr_web_link(bank_id, bank_account, amount, "Thanh toán tiền thuê phòng")
print("🔗 Link VietQR trên web:", bank_qr)


# Chọn phương thức thanh toán
print("\nChọn phương thức thanh toán:")
print("1. MoMo")
print("2. ZaloPay")
print("3. Ngân hàng (VietQR)")
choice = input("Nhập lựa chọn (1/2/3): ").strip()

if choice == "1":
    momo_link = get_momo_payment_link(amount)
    print(" Thành công! Link thanh toán MoMo:")
    print( momo_link)

elif choice == "2":
    zalopay_response = create_zalopay_payment(amount, email)
    if zalopay_response["return_code"] == 1:
        print(" Thành công! Link thanh toán ZaloPay:")
        print( zalopay_response["order_url"])
    else:
        print(" Lỗi ZaloPay:", zalopay_response["return_message"])
        print(" Chi tiết:", zalopay_response.get("sub_return_code"), "-", zalopay_response.get("sub_return_message"))

elif choice == "3":
    bank_qr = generate_vietqr_web_link(bank_id, bank_account, amount, "Thanh toán tiền thuê phòng")
    print("🔗 Link VietQR trên web:", bank_qr)
else:
    print(" Lựa chọn không hợp lệ!")
