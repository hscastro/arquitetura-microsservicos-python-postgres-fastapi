from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class PaymentBase(BaseModel):
    order_id: int
    amount: float


class PaymentCreate(PaymentBase):
    pass



class PaymentUpdate(BaseModel):
    status: Optional[str] = None



class PaymentResponse(PaymentBase):
    id: int
    status: str
    created_at: datetime

    class Config:
        from_attributes = True