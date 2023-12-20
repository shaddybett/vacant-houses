# add_sample_data.py

from database import init_database, run_migrations, add_sample_data

if __name__ == "__main__":
    init_database()
    run_migrations()
    add_sample_data()
