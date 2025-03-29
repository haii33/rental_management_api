import logging

# Cấu hình logger
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def log_info(message: str):
    """Ghi log thông tin"""
    logging.info(message)

def log_error(message: str):
    """Ghi log lỗi"""
    logging.error(message)
