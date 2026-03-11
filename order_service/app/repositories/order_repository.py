
from sqlalchemy.orm import Session
from app.models.order import Order


def get_all(db: Session):
    return db.query(Order).all()


def get_by_id(db: Session, order_id: int):
    return db.query(Order).filter(Order.id == order_id).first()


def create(db: Session, order):
    db_order = Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def update(db: Session, db_order, order_data):
    for key, value in order_data.dict().items():
        setattr(db_order, key, value)

    db.commit()
    db.refresh(db_order)
    return db_order


def delete(db: Session, db_order):
    db.delete(db_order)
    db.commit()