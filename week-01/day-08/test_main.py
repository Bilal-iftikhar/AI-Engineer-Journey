
import pytest
import main 
from services import employee_service
from fastapi.testclient import TestClient

client = TestClient(main.app)


@pytest.fixture(autouse=True)
def reset_employees():
    employee_service.employee_list[:] = [
        {"id": 1, "name": "Ali", "department": "IT"},
        {"id": 2, "name": "Ahmed", "department": "HR"}
    ]

def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Welcome to Employee Management API"


# def test_delete_employee_not_found():
#     response = client.delete("/employees/999")

#     assert response.status_code == 404



def test_get_paginated_employee():
    response = client.get("/employees/paginated?limit=10&skip=0")
    assert response.status_code == 200
    data = response.json()
    assert data["total"] == 2
    assert data["skip"] == 0
    assert data["limit"] == 10
    assert len(data["employees"]) == 2

def test_get_paginated_employee_1():
    response = client.get("/employees/paginated?limit=1&skip=1")

    assert response.status_code == 200
    data = response.json()
    assert data["skip"] == 1
    assert data["limit"] == 1
    assert len(data["employees"]) == 1
    assert data["employees"][0]["id"] == 2

def test_get_paginated_employee_invalid():
    response = client.get("/employees/paginated?limit=150")

    assert response.status_code == 422