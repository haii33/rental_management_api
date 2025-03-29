from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_chat_with_ai():
    response = client.post("/chatbot/chat", json={"message": "Hello!"})
    assert response.status_code == 200
    assert "message" in response.json()
    assert len(response.json()["message"]) > 0