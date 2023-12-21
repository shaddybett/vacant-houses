# models.py

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid

def generate_uuid():
    return str(uuid.uuid4())

Base = declarative_base()

class House(Base):
    __tablename__ = 'houses'
    houseid = Column('houseId', String, primary_key=True, default=generate_uuid)
    location = Column('location', String)
    bedrooms = Column('bedrooms', Integer)
    price = Column('price', Integer)

    def __init__(self, location, bedrooms, price):
        self.location = location
        self.bedrooms = bedrooms
        self.price = price
