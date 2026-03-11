from pydantic import BaseModel


class ItemBase(BaseModel):
    user_id: int
    product_id: int
    quantity: int
    price: float
    created_at: str


class ItemCreate(UserBase):
    pass


class ItemUpdate(UserBase):
    pass


class ItemResponse(UserBase):
    id: int

    class Config:
        from_attributes = True