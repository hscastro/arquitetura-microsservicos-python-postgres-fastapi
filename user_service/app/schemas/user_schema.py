from datetime import datetime
from pydantic import BaseModel, Field


class UserBase(BaseModel):
    email: str
    password_hash: str = Field(min_length=6, max_length=12)
    role: str
    created_at: datetime


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True