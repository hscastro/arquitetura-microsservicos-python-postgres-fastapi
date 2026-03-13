from pydantic import BaseModel


class NotificationBase(BaseModel):
    email: str
    sms: str


class NotificationCreate(NotificationBase):
    pass


class NotificationUpdate(NotificationBase):
    pass


class NotificationResponse(NotificationBase):
    id: int

    class Config:
        from_attributes = True