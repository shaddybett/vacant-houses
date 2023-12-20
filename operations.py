# operations.py

from models import session, House

def add_house(location, bedrooms, price):
    exists = session.query(House).filter_by(location=location).first()
    if exists:
        print('Location exists')
    else:
        new_house = House(location=location, bedrooms=bedrooms, price=price)
        session.add(new_house)
        session.commit()

def get_house_details(location):
    house = session.query(House).filter_by(location=location).first()
    if house:
        print(f"Location: {house.location}")
        print(f"Bedrooms: {house.bedrooms}")
        print(f"Price: {house.price}")
    else:
        print(f"No house found for location: {location}")
