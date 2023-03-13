from fastapi import FastAPI
from app.routers import item, user

app = FastAPI()

app.include_router(user.router_user_login)
app.include_router(user.router_user)
app.include_router(item.router_item)
app.include_router(item.router_item_categorical)