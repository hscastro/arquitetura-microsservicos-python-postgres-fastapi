
from sqlalchemy.orm import Session
from app.models.user import User


def get_all(db: Session):
    return db.query(User).all()


def get_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def create(db: Session, user):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update(db: Session, db_user, user_data):
    for key, value in user_data.dict().items():
        setattr(db_user , key, value)

    db.commit()
    db.refresh(db_user)
    return db_user


def delete(db: Session, db_user):
    db.delete(db_user)
    db.commit()