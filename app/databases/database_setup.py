from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("postgresql://zachrqkq:Dg7jthN8WEiXs8WwHm61Z0hJzUju_fhW@rogue.db.elephantsql.com/zachrqkq",echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)