from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from ..models import User
from ..repositories import get_user_by_email, create_user
from dotenv import load_dotenv
import os

load_dotenv()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:
    def __init__(self, db):
        self.db = db

    def create_user(self, user_data):
        hashed_password = pwd_context.hash(user_data.password)
        user = User(email=user_data.email, password=hashed_password)
        return create_user(self.db, user)

    def authenticate_user(self, email: str, password: str):
        user = get_user_by_email(self.db, email)
        if not user or not pwd_context.verify(password, user.password):
            return None
        return user

    def create_access_token(self, email: str):
        expires = datetime.utcnow() + timedelta(minutes=30)
        token = jwt.encode({"sub": email, "exp": expires}, os.getenv("SECRET_KEY"), algorithm=os.getenv("ALGORITHM"))
        return token