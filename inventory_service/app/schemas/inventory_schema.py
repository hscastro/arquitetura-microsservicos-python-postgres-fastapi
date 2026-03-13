from pydantic import BaseModel


class InventoryBase(BaseModel):
    product_id: int
    quantity_available: int
    reserved_quantity: int


class InventoryCreate(InventoryBase):
    pass


class InventoryUpdate(InventoryBase):
    pass


class InventoryResponse(InventoryBase):
    id: int

    class Config:
        from_attributes = True