def test_search_employees(client):
    response = client.get("/employees/search")

    assert response.status_code == 200
    assert "employees" in response.json()
    assert "total" in response.json()


def test_search_by_department(client, test_department):
    response = client.get(
        "/employees/search?department_id=2"
    )

    assert response.status_code == 200

    for employee in response.json()["employees"]:
        assert employee["department_id"] == 2


def test_invalid_page(client):
    response = client.get("/employees/search?page=0")

    assert response.status_code == 422


def test_invalid_limit(client):
    response = client.get("/employees/search?limit=150")

    assert response.status_code == 422


def test_invalid_sort_by(client):
    response = client.get(
        "/employees/search?sort_by=address"
    )

    assert response.status_code == 400


def test_invalid_order(client):
    response = client.get(
        "/employees/search?order=random"
    )

    assert response.status_code == 400