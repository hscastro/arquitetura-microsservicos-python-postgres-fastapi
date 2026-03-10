from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories import product_repository


def get_products(db: Session):
    return product_repository.get_all(db)


def get_product(db: Session, product_id: int):
    product = product_repository.get_by_id(db, product_id)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product


def create_product(db: Session, product):
    return product_repository.create(db, product)


def update_product(db: Session, product_id: int, product_data):
    product = product_repository.get_by_id(db, product_id)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product_repository.update(db, product, product_data)


def delete_product(db: Session, product_id: int):
    product = product_repository.get_by_id(db, product_id)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    product_repository.delete(db, product)