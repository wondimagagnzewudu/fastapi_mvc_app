from pydantic import BaseModel, Field

class PostCreate(BaseModel):
    text: str = Field(..., max_length=100000)  # 1 MB limit

class PostResponse(BaseModel):
    id: int
    text: str