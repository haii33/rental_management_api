import pytest

def test_make_payment(client):
    response = client.post("/payments/", json={
        "tenant_id": 1,
        "amount": 5000000,
        "payment_method": "momo"
    })
    assert response.status_code == 201
    assert response.json()["message"] == "Thanh toán thành công!"