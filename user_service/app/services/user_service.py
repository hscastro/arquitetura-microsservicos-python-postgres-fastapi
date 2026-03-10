from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories import user_repository


def get_users(db: Session):
    return user_repository.get_all(db)


def get_user(db: Session, user_id: int):
    user = user_repository.get_by_id(db, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


def create_user(db: Session, user):
    return user_repository.create(db, user)


def update_user(db: Session, user_id: int, user_data):
    user = user_repository.get_by_id(db, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user_repository.update(db, user, user_data)


def delete_user(db: Session, user_id: int):
    user = user_repository.get_by_id(db, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user_repository.delete(db, user)