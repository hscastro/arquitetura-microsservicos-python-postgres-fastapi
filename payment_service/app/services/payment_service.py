from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories import payment_repository


def get_payments(db: Session):
    return payment_repository.get_all(db)


def get_payment(db: Session, payment_id: int):
    payment = payment_repository.get_by_id(db, payment_id)

    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")

    return payment


def create_payment(db: Session, payment):
    return payment_repository.create(db, payment)


def update_payment(db: Session, payment_id: int, payment_data):
    payment = payment_repository.get_by_id(db, payment_id)

    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")

    return payment_repository.update(db, payment, payment_data)


def delete_payment(db: Session, payment_id: int):
    payment = payment_repository.get_by_id(db, payment_id)

    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")

    payment_repository.delete(db, payment)