from sqlalchemy.orm import Session
from app.models.user import User
from datetime import datetime
from passlib.context import CryptContext



pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_all(db: Session):
    return db.query(User).all()


def get_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def hash_password(password: str) -> str:
    password = password[:72]
    return pwd_context.hash(password)

# def hash_password(password: str) -> str:
#     return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def generator_date_now_formatated():
    data = datetime.now()
    data_formatada = data.strftime("%d/%m/%Y %H:%M")
    return data

def create(db: Session, user):
    user.created_at = generator_date_now_formatated()
    password = hash_password(user.password_hash)
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