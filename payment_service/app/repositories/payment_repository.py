
from sqlalchemy.orm import Session
from app.models.payment import Payment


def get_all(db: Session):
    return db.query(Payment).all()


def get_by_id(db: Session, payment_id: int):
    return db.query(Payment).filter(Payment.id == payment_id).first()


def create(db: Session, payment):
    db_payment = Payment(
        order_id=payment.order_id,
        amount=payment.amount,
        status="SUCCESS"
    )

    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)

    return db_payment

def update(db: Session, db_payment, payment_data):
    for key, value in payment_data.dict().items():
        setattr(db_payment, key, value)

    db.commit()
    db.refresh(db_payment)
    return db_payment

def delete(db: Session, db_payment):
    db.delete(db_payment)
    db.commit()