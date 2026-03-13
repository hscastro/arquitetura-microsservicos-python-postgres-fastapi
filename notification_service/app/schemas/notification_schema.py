from datetime import datetime
from pydantic import BaseModel
from typing import Optional



class NotificationBase(BaseModel):
    type: str
    recipient: str
    message: str
    status: Optional[str] = None



class NotificationCreate(NotificationBase):
    pass


class NotificationUpdate(NotificationBase):
    pass


class NotificationResponse(NotificationBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True