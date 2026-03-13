from sqlalchemy import Column, Integer
from app.database import Base

class Inventory(Base):
    __tablename__ = "inventaries"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, nullable=False)
    quantity_available = Column(Integer, nullable=False)
    reserved_quantity = Column(Integer, nullable=False)


