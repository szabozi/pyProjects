from assets import add_create as add
from assets import search_apotheke as search
from assets import unique_complaints as complaints

response = input("Do you wish to 'Add'(a) or 'Search'(s) : ")

valid_user_inputs = {"Add", "a", "Search", "s"}

if response in valid_user_inputs:
    if response.lower() == "add" or response.lower() == "a":
        # Create or Add new medicine
        add.add_create()
    elif response.lower() == "search" or response.lower() == "s":
        # Print unique complaints first
        complaints.print_unique_complaints()

        # Searching for a certain illness
        complaint = input("Enter your complaint: ")
        search.search_complaint(complaint)
else:
    print("Wrong input. Please enter 'Add', 'a', 'search' or 's'.")
