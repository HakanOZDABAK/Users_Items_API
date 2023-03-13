from database_setup import Base, engine
from models.item import Item
from models.user import User

print("Creating tables")

Base.metadata.create_all(engine) 
