import json
import os.path


def add_create():
    # ANSI escape character for green color
    green_color = "\033[92;3m"
    reset_color = "\033[0m"

    data = {}

    # Input values from the user
    data['name'] = input("Enter medicine name: ")
    data['type'] = input("Enter medicine type (ointment, capsule, etc.): ")
    complaints = input("What complaint is it for (head, back, tooth, nausea, etc.): ")
    data['complaint'] = [
        complaint.strip() for complaint in complaints.split(",")
    ]
    data['usage'] = input("Enter medicine's usage: ")

    # Check if the JSON file already exists
    if os.path.isfile('jsonFile/apotheke.json'):
        with open('jsonFile/apotheke.json', 'r') as file:
            existing_data = json.load(file)

        # Append the existing JSON file with new data
        existing_data.append(data)

        with open('jsonFile/apotheke.json', 'w') as file:
            json.dump(existing_data, file, indent=4)

    else:
        # Create a new JSON file with the provided data
        with open('jsonFile/apotheke.json', 'w') as file:
            json.dump([data], file, indent=4)

    print(f"\n{green_color}Medicine added successfully!{reset_color}")
    