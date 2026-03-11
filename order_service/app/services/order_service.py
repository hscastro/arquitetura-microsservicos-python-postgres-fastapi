from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories import order_repository
from app.models.order import Order
from app.models.order_item import OrderItem

def get_orders(db: Session):
    return order_repository.get_all(db)


def get_order(db: Session, order_id: int):
    order = order_repository.get_by_id(db, order_id)

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    return order



def create_order(db: Session, order_data):

    total_price = sum(
        item.quantity * item.price for item in order_data.items
    )

    order = Order(
        user_id=order_data.user_id,
        status="created",
        total_price=total_price
    )

    db.add(order)
    db.commit()
    db.refresh(order)

    for item in order_data.items:

        order_item = OrderItem(
            order_id=order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price=item.price
        )

        db.add(order_item)

    db.commit()
    db.refresh(order)

    return order

def update_order(db: Session, order_id: int, order_data):
    order = order_repository.get_by_id(db, order_id)

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    return order_repository.update(db, order, order_data)


def delete_order(db: Session, order_id: int):
    order = order_repository.get_by_id(db, order_id)

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    order_repository.delete(db, order)