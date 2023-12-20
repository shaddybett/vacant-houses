# database.py

from models import Base, engine
from alembic.config import Config
from alembic import command

def init_database():
    Base.metadata.create_all()

def run_migrations():
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")

if __name__ == "__main__":
    init_database()
    run_migrations()
