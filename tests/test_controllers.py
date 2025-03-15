from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_signup():
    # Test /signup endpoint
    response = client.post("/signup", json={"email": "test@example.com", "password": "password"})
    assert response.status_code == 200
    assert "token" in response.json()

def test_login():
    # Test /login endpoint
    client.post("/signup", json={"email": "test@example.com", "password": "password"})
    response = client.post("/login", json={"email": "test@example.com", "password": "password"})
    assert response.status_code == 200
    assert "token" in response.json()

def test_add_post():
    # Test /addpost endpoint
    # First, sign up and log in to get a token
    client.post("/signup", json={"email": "test@example.com", "password": "password"})
    login_response = client.post("/login", json={"email": "test@example.com", "password": "password"})
    token = login_response.json()["token"]
    # Add a post
    response = client.post(
        "/addpost",
        json={"text": "Test post"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    assert "postID" in response.json()

def test_get_posts():
    # Test /getposts endpoint
    # First, sign up and log in to get a token
    client.post("/signup", json={"email": "test@example.com", "password": "password"})
    login_response = client.post("/login", json={"email": "test@example.com", "password": "password"})
    token = login_response.json()["token"]
    # Add a post
    client.post(
        "/addpost",
        json={"text": "Test post"},
        headers={"Authorization": f"Bearer {token}"},
    )
    # Get posts
    response = client.get(
        "/getposts",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    assert len(response.json()) > 0