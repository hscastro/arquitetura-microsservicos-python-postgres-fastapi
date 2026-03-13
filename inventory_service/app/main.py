from fastapi import FastAPI
from app.database import Base, engine
from app.routers import inventory_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(inventory_router.router)