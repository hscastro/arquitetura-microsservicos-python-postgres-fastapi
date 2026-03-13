from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories import notification_repository


def get_notifications(db: Session):
    return notification_repository.get_all(db)


def get_notification(db: Session, notification_id: int):
    notification = notification_repository.get_by_id(db, notification_id)

    if not notification:
        raise HTTPException(status_code=404, detail="Notification not found")

    return notification


def create_notification(db: Session, notification):
    return notification_repository.create(db, notification)


def update_notification(db: Session, notification_id: int, notification_data):
    notification = notification_repository.get_by_id(db, notification_id)

    if not notification:
        raise HTTPException(status_code=404, detail="Notification not found")

    return notification_repository.update(db, notification, notification_data)


def delete_notification(db: Session, notification_id: int):
    notification = notification_repository.get_by_id(db, notification_id)

    if not notification:
        raise HTTPException(status_code=404, detail="Notification not found")

    notification_repository.delete(db, notification)