# cli.py

import argparse
from operations import get_house_details, list_all_houses

def main():
    parser = argparse.ArgumentParser(description="House Database CLI")
    parser.add_argument("--get-details", help="Get details for a specific location")

    args = parser.parse_args()

    if args.get_details:
        get_house_details(args.get_details)
    else:
        list_all_houses()

if __name__ == "__main__":
    main()
