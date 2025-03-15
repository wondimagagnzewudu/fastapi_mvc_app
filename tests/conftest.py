import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.base import Base

# Fixture for the database session
@pytest.fixture(scope="module")
def db_session():
    # Use an in-memory SQLite database for testing
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

# Fixture for the FastAPI test client
@pytest.fixture(scope="module")
def test_client():
    from app.main import app
    from fastapi.testclient import TestClient
    client = TestClient(app)
    yield client