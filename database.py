# database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, House

# Define the engine
db_url = 'sqlite:///houseDB.db'
engine = create_engine(db_url)

# Bind the engine to the Base class
Base.metadata.bind = engine

# Create a session factory
Session = sessionmaker(bind=engine)

# Create a session
session = Session()

def init_database():
    # Create tables
    Base.metadata.create_all(bind=engine)

def run_migrations():
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")

def add_sample_data():
    # Add sample houses
    houses_data = [
        {"location": "Ngong", "bedrooms": 3, "price": 200000},
        {"location": "Karen", "bedrooms": 4, "price": 250000},
        {"location": "Runda", "bedrooms": 5, "price": 300000},
    ]

    with session.begin():
        for data in houses_data:
            house = House(**data)
            session.add(house)

if __name__ == "__main__":
    init_database()
    run_migrations()
    add_sample_data()
