import json


def print_unique_complaints():
    # ANSI escape character for green color
    green_color = "\033[92;3m"
    reset_color = "\033[0m"

    with open('jsonFile/apotheke.json', 'r') as file:
        data = json.load(file)

    unique_complaints = set()
    for item in data:
        unique_complaints.update(item['complaint'])

    sorted_complaints = sorted(unique_complaints)
    unique_complaints_str = ", ".join(sorted_complaints)
    print(f"\nWe have medicine for the following complaints: {green_color}{unique_complaints_str}{reset_color}\n")
