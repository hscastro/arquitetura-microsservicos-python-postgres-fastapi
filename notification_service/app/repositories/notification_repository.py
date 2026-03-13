from sqlalchemy.orm import Session
from app.models.notification import Notification


def get_all(db: Session):
    return db.query(Notification).all()


def get_by_id(db: Session, notification_id: int):
    return db.query(Notification).filter(Notification.id == notification_id).first()


def create(db: Session, notification):
    db_notification = Notification(**notification.dict())
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)
    return db_notification


def update(db: Session, db_notification, notification_data):
    for key, value in notification_data.dict().items():
        setattr(db_notification, key, value)

    db.commit()
    db.refresh(db_notification)
    return db_notification


def delete(db: Session, db_notification):
    db.delete(db_notification)
    db.commit()