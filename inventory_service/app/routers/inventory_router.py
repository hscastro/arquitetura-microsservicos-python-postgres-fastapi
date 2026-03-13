from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.inventory_schema import InventoryCreate, InventoryUpdate, InventoryResponse
from app.services import inventory_service

router = APIRouter(prefix="/inventories", tags=["Inventories"])


@router.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "inventory_service"
    }


@router.get("/", response_model=list[InventoryResponse])
def get_inventories(db: Session = Depends(get_db)):
    return inventory_service.get_inventories(db)


@router.get("/{inventory_id}", response_model=InventoryResponse)
def get_inventory(inventory_id: int, db: Session = Depends(get_db)):
    return inventory_service.get_inventory(db, inventory_id)


@router.post("/", response_model=InventoryResponse)
def create_inventory(inventory: InventoryCreate, db: Session = Depends(get_db)):
    return inventory_service.create_inventory(db, inventory)


@router.put("/{inventory_id}", response_model=InventoryResponse)
def update_inventory(inventory_id: int, inventory: InventoryUpdate, db: Session = Depends(get_db)):
    return inventory_service.update_inventory(db, inventory_id, inventory)


@router.delete("/{inventory_id}")
def delete_inventory(inventory_id: int, db: Session = Depends(get_db)):
    inventory_service.delete_inventory(db, inventory_id)
    return {"message": "Inventory deleted"}