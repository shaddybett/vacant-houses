# cli.py

from operations import add_house, get_house_details

def add_house_cli():
    location = input("Enter location: ")
    bedrooms = int(input("Enter number of bedrooms: "))
    price = int(input("Enter price: "))

    add_house(location, bedrooms, price)
    print("House added successfully!")

def get_house_details_cli():
    location = input("Enter location to get details: ")
    get_house_details(location)

if __name__ == "__main__":
    print("1. Add a house")
    print("2. Get house details")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        add_house_cli()
    elif choice == "2":
        get_house_details_cli()
    else:
        print("Invalid choice")
