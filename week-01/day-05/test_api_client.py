
import pytest
import requests
from unittest.mock import patch, Mock

from api_client import ApiClient


@pytest.fixture
def client():
    return ApiClient()


# -------------------------------
# Test 1: Get all posts
# -------------------------------
@patch("api_client.requests.get")
def test_get_all_posts(mock_get, client):

    mock_response = Mock()
    mock_response.json.return_value = [
        {"userId": 1, "id": 1, "title": "Post 1"},
        {"userId": 1, "id": 2, "title": "Post 2"}
    ]

    mock_get.return_value = mock_response

    posts = client.get_all_posts()

    assert isinstance(posts, list)
    assert len(posts) == 2
    assert posts[0]["title"] == "Post 1"

    mock_get.assert_called_once_with(
        "https://jsonplaceholder.typicode.com/posts",
        timeout=10
    )


# -------------------------------
# Test 2: Get user details
# -------------------------------
@patch("api_client.requests.get")
def test_get_user_detail(mock_get, client):

    mock_response = Mock()
    mock_response.json.return_value = {
        "id": 2,
        "username": "Antonette",
        "email": "test@example.com",
        "address": {
            "city": "Wisokyburgh"
        }
    }

    mock_get.return_value = mock_response

    user = client.get_user_detail(2)

    assert user["id"] == 2
    assert user["username"] == "Antonette"
    assert user["email"] == "test@example.com"
    assert user["address"]["city"] == "Wisokyburgh"

    mock_get.assert_called_once_with(
        "https://jsonplaceholder.typicode.com/users/2",
        timeout=10
    )


# -------------------------------
# Test 3: Get post by ID
# -------------------------------
@patch("api_client.requests.get")
def test_get_post_by_id(mock_get, client):

    mock_response = Mock()
    mock_response.json.return_value = {
        "userId": 1,
        "id": 10,
        "title": "Test Post",
        "body": "This is a test post."
    }

    mock_get.return_value = mock_response

    post = client.get_post_by_id(10)

    assert post["id"] == 10
    assert post["title"] == "Test Post"
    assert post["body"] == "This is a test post."

    mock_get.assert_called_once_with(
        "https://jsonplaceholder.typicode.com/posts/10",
        timeout=10
    )


# -------------------------------
# Test 4: HTTP Error
# -------------------------------
@patch("api_client.requests.get")
def test_http_error(mock_get, client):

    mock_response = Mock()
    mock_response.raise_for_status.side_effect = (
        requests.exceptions.HTTPError("404 Not Found")
    )

    mock_get.return_value = mock_response

    with pytest.raises(requests.exceptions.HTTPError):
        client.get_post_by_id(9999)


# -------------------------------
# Test 5: Request Timeout
# -------------------------------
@patch("api_client.requests.get")
def test_request_timeout(mock_get, client):

    mock_get.side_effect = requests.exceptions.Timeout(
        "Request timed out"
    )

    with pytest.raises(requests.exceptions.Timeout):
        client.get_all_posts()


# -------------------------------
# Test 6: Connection Error
# -------------------------------
@patch("api_client.requests.get")
def test_connection_error(mock_get, client):

    mock_get.side_effect = requests.exceptions.ConnectionError(
        "Connection failed"
    )

    with pytest.raises(requests.exceptions.ConnectionError):
        client.get_all_posts()


# -------------------------------
# Test 7: Verify make_request
# -------------------------------
@patch("api_client.requests.get")
def test_make_request(mock_get, client):

    mock_response = Mock()
    mock_get.return_value = mock_response

    response = client.make_request(
        "https://jsonplaceholder.typicode.com/posts"
    )

    assert response == mock_response
    mock_response.raise_for_status.assert_called_once()

    mock_get.assert_called_once_with(
        "https://jsonplaceholder.typicode.com/posts",
        timeout=10
    )
