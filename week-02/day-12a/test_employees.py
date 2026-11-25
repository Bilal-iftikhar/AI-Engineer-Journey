def test_get_all_employees(client):
    response = client.get("/employees/")

    assert response.status_code == 200
    assert response.json() == []


def test_create_employee(client, test_department):
    response = client.post(
        "/employees/",
        json={
            "name": "Afnan",
            "email": "afnan@example.com",
            "department_id": 2,
            "salary": 60000
        }
    )

    assert response.status_code == 201
    assert response.json()["name"] == "Afnan"


def test_get_employee_not_found(client):
    response = client.get("/employees/999")

    assert response.status_code == 404


def test_duplicate_email(client, test_department):
    payload = {
        "name": "Afnan",
        "email": "afnan@example.com",
        "department_id": 2,
        "salary": 60000
    }

    first = client.post("/employees/", json=payload)
    second = client.post("/employees/", json=payload)

    assert first.status_code == 201
    assert second.status_code == 409


def test_invalid_department(client):
    response = client.post(
        "/employees/",
        json={
            "name": "TestUser",
            "email": "testuser@example.com",
            "department_id": 999,
            "salary": 50000
        }
    )

    assert response.status_code == 409