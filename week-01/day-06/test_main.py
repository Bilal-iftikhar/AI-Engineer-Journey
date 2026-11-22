
import pytest
import main
from fastapi.testclient import TestClient

client = TestClient(main.app)


# Reset employee data before every test
@pytest.fixture(autouse=True)
def reset_employees():
    main.employee_list[:] = [
        {"id": 1, "name": "Ali", "department": "IT"},
        {"id": 2, "name": "Ahmed", "department": "HR"}
    ]


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Welcome to Employee Management API"


def test_get_employees():
    response = client.get("/employees")

    assert response.status_code == 200
    assert len(response.json()) == 2


def test_filter_employees():
    response = client.get("/employees?department=IT")

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["name"] == "Ali"


def test_get_employee():
    response = client.get("/employees/1")

    assert response.status_code == 200
    assert response.json()["name"] == "Ali"


def test_add_employee():
    response = client.post(
        "/employees",
        json={
            "id": 3,
            "name": "Bilal",
            "department": "AI"
        }
    )

    assert response.status_code == 201
    assert response.json()["employee"]["name"] == "Bilal"

def test_update_employee():
    response = client.put(
        "/employees/1",
        json={
            "id": 1,
            "name": "Bilal",
            "department": "HR"
        }
    )

    assert response.status_code == 200
    assert response.json()["employee"]["department"] == "HR"


def test_get_employee_not_found():
    response = client.get("/employees/999")

    assert response.status_code == 404


def test_add_duplicate_employee():
    response = client.post(
        "/employees",
        json={
            "id": 1,
            "name": "Bilal",
            "department": "AI"
        }
    )

    assert response.status_code == 409


def test_add_employee_invalid_name():
    response = client.post(
        "/employees",
        json={
            "id": 3,
            "name": "A",
            "department": "AI"
        }
    )

    assert response.status_code == 422


def test_delete_employee():
    response = client.delete("/employees/1")

    assert response.status_code == 200
    assert response.json()["employee"]["id"] == 1

    # Verify employee was actually deleted
    get_response = client.get("/employees/1")
    assert get_response.status_code == 404


def test_delete_employee_not_found():
    response = client.delete("/employees/999")

    assert response.status_code == 404

