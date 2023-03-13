from pydantic import BaseModel


class Item(BaseModel):
    name:str
    price:float
    category:str
    on_offer:bool

    class Config:
        orm_mode = True

