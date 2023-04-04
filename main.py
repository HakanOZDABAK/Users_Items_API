from fastapi import FastAPI
from app.routers import item, user
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(user.router_user_login)
app.include_router(user.router_user)
app.include_router(item.router_item)
app.include_router(item.router_get_item_by_categorical)
app.include_router(item.router_get_item_by_name)