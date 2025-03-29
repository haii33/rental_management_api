# Rental Management API

# 1. Giới Thiệu
Dự án **Rental Management API** được phát triển bằng **FastAPI**, giúp quản lý phòng trọ với các chức năng:
- **Quản lý phòng** 
API quản lý danh sách phòng, thêm, sửa, xóa thông tin phòng.
Xem danh sách phòng còn trống.
- **Quản lý khách thuê** 
Quản lý thông tin khách thuê, hợp đồng thuê nhà.
- **Thanh toán** 
Hỗ trợ chuyển khoản ngân hàng, ZaloPay, Momo
- **Chatbot hỗ trợ khách hàng**
- **Gửi thông báo qua Email & SMS**
- **Xác thực người dùng (JWT Token)**

# 2. Cài Đặt Dự Án
# 🛠 Yêu Cầu Hệ Thống:
Python 3.10 trở lên.
SQLite hoặc cơ sở dữ liệu tương thích (PostgreSQL, MySQL, ...).
OpenAI API Key (dùng cho chatbot AI).

# Bước 1: Clone Dự Án
```sh
git clone https://github.com/haii33/rental_management_api.git
cd rental_management_api

# Bước 2: Tạo Môi Trường Ảo
python -m venv venv
# Kích hoạt môi trường ảo:
venv\Scripts\activate

# Bước 3: Cài Đặt Các Gói Yêu Cầu
pip install -r requirements.txt

# Bước 4: Cấu hình file .env: Tạo file .env trong thư mục gốc dự án và cấu hình các biến môi trường theo mẫu:
DATABASE_URL=sqlite:///./rental_management.db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30


# Bước 5: Khởi tạo database:
# Chạy Alembic để tạo bảng:
alembic revision --autogenerate -m "Fix relationships and schema"
alembic upgrade head

# Bước 6: Tải dữ liệu mẫu cho phòng:
python load_rooms_data.py

python load_dataset.py


# Bước 7: Khởi Động Dự Án
# Chạy Server FastAPI
uvicorn main:app --reload

# Bước 8: Chạy Kiểm Tra Bằng pytest
pytest tests/

