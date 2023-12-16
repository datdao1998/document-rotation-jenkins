"""
Api servermodule test
"""
import os
import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def client():
    """
    Get dataset
    """
    api_client = TestClient(app)
    return api_client


def test_check_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"Message": "Service is working"}


def test_rotate(client):
    fpath = "app/example/270_sample.jpg"
    assert os.path.isfile(fpath) == True
    with open(fpath, "rb") as f:
        r = client.post(
            "/rotate", files={"file": (os.path.basename(fpath), f, "image/jpeg")}
        )
        assert r.status_code == 200
        assert r.json() == {"statusCode": 200, "angle": "270"}
