import pytest
from httpx import AsyncClient
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
from main import app
from fastapi.testclient import TestClient

@pytest.fixture(scope="module")
def client():
    """Tạo TestClient cho pytest"""
    with TestClient(app) as client:
        yield client