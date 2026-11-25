import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_all_employees():
    response = client.get("/employees/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_employee_not_found():
    response = client.get("/employees/999999")

    assert response.status_code == 404


def test_create_employee():
    response = client.post(
        "/employees/",
        json={
            "name": "TestUser",
            "email": "pytest.unique15@example.com",
            "department_id": 2,
            "salary": 60000
        }
    )

    assert response.status_code == 201
    assert response.json()["name"] == "TestUser"


def test_duplicate_email():
    email = "pytest.duplicate14@example.com"

    payload = {
        "name": "TestUser",
        "email": email,
        "department_id": 2,
        "salary": 60000
    }

    first = client.post("/employees/", json=payload)
    assert first.status_code == 201

    second = client.post("/employees/", json=payload)
    assert second.status_code == 409