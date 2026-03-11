import bcrypt
from sqlalchemy.orm import Session
from app.models.user import User
from datetime import datetime


def get_all(db: Session):
    return db.query(User).all()


def get_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def generated_password_hash(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password, salt)

def generator_date_now_formatated():
    data = datetime.now()
    data_formatada = data.strftime("%d/%m/%Y %H:%M")
    return data

def create(db: Session, user):
    user.created_at = generator_date_now_formatated()
    pass_ = user.password_hash
    password = generated_password_hash(pass_)
    user.password_hash = password

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