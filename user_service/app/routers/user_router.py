from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.user_schema import UserCreate, UserUpdate, UserResponse
from app.services import user_service

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "user_service"
    }


@router.get("/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return user_service.get_users(db)


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return user_service.get_user(db, user_id)


@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, user)


@router.put("/{user_id}", response_model=UserResponse)
def update_product(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    return user_service.update_user(db, user_id, user)


@router.delete("/{user_id}")
def delete_product(user_id: int, db: Session = Depends(get_db)):
    user_service.delete_user(db, user_id)
    return {"message": "User deleted"}