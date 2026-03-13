from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.notification_schema import NotificationCreate, NotificationUpdate, NotificationResponse
from app.services import notification_service

router = APIRouter(prefix="/notifications", tags=["Notifications"])


@router.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "Notification_service"
    }


@router.get("/", response_model=list[NotificationResponse])
def get_notifications(db: Session = Depends(get_db)):
    return notification_service.get_notifications(db)


@router.get("/{notification_id}", response_model=NotificationResponse)
def get_notification(notification_id: int, db: Session = Depends(get_db)):
    return notification_service.get_notification(db, notification_id)


@router.post("/", response_model=NotificationResponse)
def create_notification(notification: NotificationCreate, db: Session = Depends(get_db)):
    return notification_service.create_notification(db, notification)


@router.put("/{notification_id}", response_model=NotificationResponse)
def update_notification(notification_id: int, notification: NotificationUpdate, db: Session = Depends(get_db)):
    return notification_service.update_inventory(db, notification_id, notification)


@router.delete("/{notification_id}")
def delete_notification(notification_id: int, db: Session = Depends(get_db)):
    notification_service.delete_notification(db, notification_id)
    return {"message": "Notification deleted"}