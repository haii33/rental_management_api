from fastapi import APIRouter, HTTPException
import openai
from pydantic import BaseModel
from decouple import config

# Đọc API Key từ file .env
openai.api_key = config("OPENAI_API_KEY")

# Khởi tạo router cho chatbot
router = APIRouter()

# Định nghĩa API Key của OpenAI (Cấu hình qua file .env)
openai.api_key = "YOUR_OPENAI_API_KEY"  # Thay YOUR_OPENAI_API_KEY bằng API key của bạn

class ChatRequest(BaseModel):
    message: str

@router.post("/ chat")
async def chat_with_ai(chat_request: ChatRequest):
    """
    Chat với AI để trả lời câu hỏi của người dùng
    """
    try:
        # Gửi yêu cầu tới OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Hoặc gpt-4 nếu bạn có quyền truy cập
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": chat_request.message}
            ],
            max_tokens=150,
            temperature=0.7
        )
        # Lấy câu trả lời từ AI
        ai_reply = response['choices'][0]['message']['content']
        return {"message": ai_reply}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI Error: {str(e)}")