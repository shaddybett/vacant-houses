# models.py

from sqlalchemy import create_engine, Column, String, Integer, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class House(Base):
    __tablename__ = 'houses'
    houseid = Column('houseId', String, primary_key=True)
    location = Column('location', String)
    bedrooms = Column('bedrooms', Integer)
    price = Column('price', Integer)

# Define engine and metadata
db_url = 'sqlite:///houseDB.db'
engine = create_engine(db_url)
metadata = MetaData()

# Bind the engine and metadata to the base
Base.metadata.bind = engine
metadata.bind = engine

# Create a session
Session = sessionmaker(bind=engine)
session = Session()
