from typing import List
from fastapi import APIRouter, HTTPException, status
from app.schemas.item import Item
from app.databases.models.item import Item as ItemDB
from app.databases.database_setup import SessionLocal
from app.schemas.user import User

router_item = APIRouter(
    prefix='/items',
    tags=['Items']

)
router_get_item_by_categorical = APIRouter(
    prefix='/items_get_by',
    tags=['Items']

)

router_get_item_by_name = APIRouter(
    prefix='/items_get_by_name',
    tags=['Items']

)


db = SessionLocal()


@router_item.get("/", response_model=List[Item], status_code=status.HTTP_200_OK)
def all_item_get():
    items = db.query(ItemDB).all()
    return items


@router_item.get('/{id}', response_model=Item, status_code=status.HTTP_200_OK)
def item_get(id: int,):
    item = db.query(ItemDB).filter(ItemDB.id == id).first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Item with id {id} not found")

    return item


@router_item.post('/add',response_model=Item, status_code=status.HTTP_201_CREATED)
def item_post(item: Item,):
    item = ItemDB(
                  name = item.name,
                  price = item.price,
                  category = item.category,
                  on_offer = item.on_offer
                  )
    db.add(item)
    db.commit()
    return item


@router_item.delete('/delete/{id}', status_code=status.HTTP_200_OK)
def item_delete(id: int,):
    item = db.query(ItemDB).filter(ItemDB.id == id).first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Item with id {id} not found")
    db.delete(item)
    db.commit()
    return f"Item with id = {id} deleted"


@router_get_item_by_categorical.get('/{category}',response_model=List[Item])
def get_item_by_categorical(category:str,):
    items = db.query(ItemDB).filter(ItemDB.category == category).all()
    if items is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return items



@router_get_item_by_name.get('/{name}',response_model = Item)
def get_item_by_name(name:str):
    item = db.query(ItemDB).filter(ItemDB.name==name).first()
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return item