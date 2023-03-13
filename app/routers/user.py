from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from app.JWT.oat2 import get_current_user
from app.JWT.token import create_access_token
from app.schemas.user import ShowUser, User
from app.databases.models.user import User as UserDB
from app.databases.database_setup import SessionLocal
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router_user_login = APIRouter(
    prefix='/login',
    tags=['Authentication']

)

router_user = APIRouter(
    prefix='/user',
    tags=['User']

)

db = SessionLocal()

@router_user_login.post('/', status_code=status.HTTP_200_OK)
def login_user(request: OAuth2PasswordRequestForm = Depends() ):
    user_db = db.query(UserDB).filter(UserDB.name == request.username).first()
    if user_db is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    else:
     passwordCheck = pwd_context.verify(request.password, user_db.password)
     if passwordCheck is True:
        access_token = create_access_token(
         data={"sub": user_db.name}
        )
        return {"access_token": access_token, "token_type": "bearer"}
     else:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)


@router_user.get("/", response_model=List[ShowUser], status_code=status.HTTP_200_OK)
def all_user_get(get_current_user:User = Depends(get_current_user)):
    users = db.query(UserDB).all()
    return users


@router_user.get('/{id}', response_model=ShowUser, status_code=status.HTTP_200_OK)
def user_get(id: int,get_current_user:User = Depends(get_current_user)):
    user = db.query(UserDB).filter(UserDB.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} not found")

    return user


@router_user.post('/add', response_model=ShowUser, status_code=status.HTTP_201_CREATED)
def user_post(user: User):
    hashed_password = pwd_context.hash(user.password)
    user = UserDB(
                  name=user.name,
                  email=user.email,
                  password=hashed_password)
    db.add(user)
    db.commit()
    return user


@router_user.delete('/delete/{id}', status_code=status.HTTP_200_OK)
def user_delete(id: int,get_current_user:User = Depends(get_current_user)):
    user = db.query(UserDB).filter(UserDB.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} not found")
    db.delete(user)
    db.commit()
    return f"User with id = {id} deleted"



