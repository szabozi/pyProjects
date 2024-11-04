import json


def search_complaint(complaint):

    # ANSI escape character for green color
    green_color = "\033[92;3m"
    reset_color = "\033[0m"

    with open('jsonFile/apotheke.json', 'r') as file:
        data = json.load(file)

    found = False
    for item in data:
        if complaint in item['complaint']:
            found = True
            print(f"\nMedicine name: {green_color}{item['name']}{reset_color}")
            print(f"Medicine type: {green_color}{item['type']}{reset_color}")
            print(f"Usage: {green_color}{item['usage']}{reset_color}")
            print()

    if not found:
        print("I am sorry, i have no record of such complaint..")