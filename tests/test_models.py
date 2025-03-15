from app.models import User, Post

def test_user_model(db_session):
    # Test User model
    user = User(email="test@example.com", password="password")
    db_session.add(user)
    db_session.commit()
    assert user.id is not None
    assert user.email == "test@example.com"

def test_post_model(db_session):
    # Test Post model
    user = User(email="test@example.com", password="password")
    db_session.add(user)
    db_session.commit()
    post = Post(text="Test post", owner_id=user.id)
    db_session.add(post)
    db_session.commit()
    assert post.id is not None
    assert post.text == "Test post"
    assert post.owner_id == user.id