from fastapi import FastAPI

from .customer_routes import router

app = FastAPI()
app.include_router(router, prefix="/customer")
