from datetime import datetime, timedelta
from jose import JWTError, jwt
from app.schemas.token import TokenData

SECRET_KEY = "YOUR SECRET KEY"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(data:str, credentials_exception):
    try:
        payload = jwt.decode(data, SECRET_KEY, algorithms=[ALGORITHM])
        name: str = payload.get("sub")
        if name is None:
            raise credentials_exception
        token_Data = TokenData(name=name)
    except JWTError:
        raise credentials_exception
