import pytest

def test_create_tenant(client):
    response = client.post("/tenants/", json={
        "name": "Trần Văn B",
        "phone": "0987654321",
        "email": "tenant@example.com",
        "room_id": 1
    })
    assert response.status_code == 201
    assert response.json()["message"] == "Thêm khách thuê thành công!"