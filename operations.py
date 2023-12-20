# operations.py

from models import session, House

def get_house_details(location):
    house = session.query(House).filter_by(location=location).first()
    if house:
        print(f"Location: {house.location}")
        print(f"Bedrooms: {house.bedrooms}")
        print(f"Price: {house.price}")
    else:
        print(f"No house found for location: {location}")

# Optionally, you can add a function to list all houses
def list_all_houses():
    houses = session.query(House).all()
    if houses:
        for house in houses:
            print(f"Location: {house.location}, Bedrooms: {house.bedrooms}, Price: {house.price}")
    else:
        print("No houses found in the database.")
