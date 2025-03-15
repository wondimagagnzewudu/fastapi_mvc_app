from fastapi import FastAPI
from .controllers import router
from .models.base import Base, engine

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routes
app.include_router(router)