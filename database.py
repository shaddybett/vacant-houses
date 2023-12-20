# database.py

from models import Base, engine, session, House
from alembic.config import Config
from alembic import command

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

    for data in houses_data:
        house = House(**data)
        session.add(house)

    session.commit()

if __name__ == "__main__":
    init_database()
    run_migrations()
    add_sample_data()
