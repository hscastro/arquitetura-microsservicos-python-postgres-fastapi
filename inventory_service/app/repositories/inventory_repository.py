from sqlalchemy.orm import Session
from app.models.inventory import Inventory


def get_all(db: Session):
    return db.query(Inventory).all()


def get_by_id(db: Session, inventory_id: int):
    return db.query(Inventory).filter(Inventory.id == inventory_id).first()


def create(db: Session, inventory):
    db_inventory = Inventory(**inventory.dict())
    db.add(db_inventory)
    db.commit()
    db.refresh(db_inventory)
    return db_inventory


def update(db: Session, db_inventory, inventory_data):
    for key, value in inventory_data.dict().items():
        setattr(db_inventory, key, value)

    db.commit()
    db.refresh(db_inventory)
    return db_inventory


def delete(db: Session, db_inventory):
    db.delete(db_inventory)
    db.commit()