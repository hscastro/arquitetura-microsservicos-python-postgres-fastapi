import datetime
from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    password_hash: str
    role: str
    created_at: str


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True