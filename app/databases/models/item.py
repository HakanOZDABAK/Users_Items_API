from sqlalchemy import Boolean, Column, Integer, String, Float
import sys
sys.path.append("..")
from ..database_setup import Base

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True,unique=True,autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)
    price = Column(Float,nullable=False)
    category = Column(String(255),nullable=False)
    on_offer = Column(Boolean, default=True,nullable=False)

