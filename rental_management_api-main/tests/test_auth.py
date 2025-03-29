import pytest
def test_register(client):
    response = client.post("/auth/register", json={
        "full_name": "Nguyễn Văn A",
        "email": "user@example.com",
        "phone_number": "0123456789",
        "identity_card": "123456789",
        "password": "mypassword",
        "role": "tenant"
    })
    assert response.status_code == 201
    assert response.json()["message"] == "Đăng ký thành công!"

def test_login(client):
    response = client.post("/auth/login", json={
        "email": "user@example.com",
        "password": "mypassword"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()