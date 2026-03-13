from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories import inventory_repository


def get_inventories(db: Session):
    return inventory_repository.get_all(db)


def get_inventory(db: Session, inventory_id: int):
    inventory = inventory_repository.get_by_id(db, inventory_id)

    if not inventory:
        raise HTTPException(status_code=404, detail="Inventory not found")

    return inventory


def create_inventory(db: Session, inventory):
    return inventory_repository.create(db, inventory)


def update_inventory(db: Session, inventory_id: int, inventory_data):
    inventory = inventory_repository.get_by_id(db, inventory_id)

    if not inventory:
        raise HTTPException(status_code=404, detail="Inventory not found")

    return inventory_repository.update(db, inventory, inventory_data)


def delete_inventory(db: Session, inventory_id: int):
    inventory = inventory_repository.get_by_id(db, inventory_id)

    if not inventory:
        raise HTTPException(status_code=404, detail="Inventory not found")

    inventory_repository.delete(db, inventory)