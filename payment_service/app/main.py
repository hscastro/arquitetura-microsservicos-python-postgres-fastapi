from fastapi import FastAPI
from app.database import Base, engine
from app.routers import payment_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(payment_router.router)