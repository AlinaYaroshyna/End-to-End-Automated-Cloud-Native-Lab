import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest

from main import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_index_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json()["message"].startswith("Hello")


def test_health_returns_healthy(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}


def test_info_contains_hostname(client):
    response = client.get("/info")
    assert response.status_code == 200
    data = response.get_json()
    assert "hostname" in data
    assert "version" in data
