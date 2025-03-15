from app.services import UserService, PostService
from app.models import User
from app.schemas import UserCreate, PostCreate

def test_create_user(db_session):
    # Test UserService.create_user
    user_service = UserService(db_session)
    user_data = UserCreate(email="test@example.com", password="password")
    user = user_service.create_user(user_data)
    assert user.email == "test@example.com"
    assert user.id is not None

def test_authenticate_user(db_session):
    # Test UserService.authenticate_user
    user_service = UserService(db_session)
    user_data = UserCreate(email="test@example.com", password="password")
    user_service.create_user(user_data)
    authenticated_user = user_service.authenticate_user("test@example.com", "password")
    assert authenticated_user is not None

def test_create_post(db_session):
    # Test PostService.create_post
    user_service = UserService(db_session)
    user_data = UserCreate(email="test@example.com", password="password")
    user = user_service.create_user(user_data)
    post_service = PostService(db_session)
    post_data = PostCreate(text="Test post")
    post = post_service.create_post(post_data, user.id)
    assert post.text == "Test post"
    assert post.owner_id == user.id