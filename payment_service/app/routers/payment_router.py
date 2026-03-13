from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.payment_schema import PaymentCreate, PaymentResponse
from app.services import payment_service

router = APIRouter(prefix="/payments", tags=["Payments"])

@router.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "Payment_service"
    }

@router.post("/", response_model=PaymentResponse)
def create_payment(payment: PaymentCreate, db: Session = Depends(get_db)):
    return payment_service.create_payment(db, payment)


@router.get("/", response_model=list[PaymentResponse])
def get_payments(db: Session = Depends(get_db)):
    return payment_service.get_payments(db)


@router.get("/{payment_id}", response_model=PaymentResponse)
def get_payment(payment_id: int, db: Session = Depends(get_db)):
    return payment_service.get_payment(db, payment_id)


@router.delete("/{payment_id}")
def delete_payment(payment_id: int, db: Session = Depends(get_db)):
    payment_service.delete_payment(db, payment_id)
    return {"message": "Payment deleted"}