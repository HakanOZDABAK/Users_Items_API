from sqlalchemy import Column, Integer, String
import sys
sys.path.append("..")
from ..database_setup import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True,unique=True,autoincrement=True)
    name = Column(String(255),nullable=False,unique=True)
    email = Column(String(255))
    password = Column(String(255),nullable=False)

    
      