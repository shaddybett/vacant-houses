# models.py

from sqlalchemy import create_engine, String, Integer, Column
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

def generate_uuid():
    return str(uuid.uuid4())

class House(Base):
    __tablename__ = 'houses'
    houseid = Column('houseId', String, primary_key=True, default=generate_uuid)
    location = Column('location', String)
    bedrooms = Column('bedrooms', Integer)
    price = Column('price', Integer)

    def __init__(self, location, bedrooms, price):
        self.houseid = None
        self.location = location
        self.bedrooms = bedrooms
        self.price = price
