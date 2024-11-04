import gspread

print("Connecting to the service account JSON file...")
serviceAccount = gspread.service_account(filename="pythonSheets.json")

print("Connecting to the actual sheet 'Book Collection and Tracker'...")
sheet = serviceAccount.open("Book Collection and Tracker")

print("Selecting the worksheet 'Book-List'...")
worksheets = sheet.worksheet("Book-List")


print("Saving all data in a variable...")
allData = worksheets.get_all_records()

print("Getting all the unique authors..")
unique_authors = set()
authors = []
for author in allData:
    authors.append(author['Author'])
    unique_authors.add(author['Author'])

sorted_unique_authors = sorted(unique_authors)
print(sorted_unique_authors)

# searching for a specific author
print("Searching for a specific author...")
author_to_search = input("Please type the authors name: ")
author_search_reasult = None
for author in sorted_unique_authors:
    if author == author_to_search:
        author_search_reasult = author

print(f"\nSearch Result: {author_search_reasult}")

# searching for authors that share the same name or names
print(f"\nSearching for authors that share the same name as '{author_to_search}'...")
name_components = author_to_search.split()
similar_authors = []
for author in sorted_unique_authors:
    if any(component.lower() in author.lower() for component in name_components):
        similar_authors.append(author)

print(f"\nAuthors with similar names: {similar_authors}")

# search for books by the searched author
author_books = []
if author_search_reasult is not None:
    print(f"\nBooks by {author_search_reasult}:")
    for record in allData:
        if record['Author'] == author_search_reasult:
            author_books.append(record['Title'])
if author_search_reasult is not None:
    print(author_books)

# search for books by authors with similar names
if similar_authors:
    for author in similar_authors:
        similar_author_books = []
        print(f"\nBooks by {author}:")
        for record in allData:
            if record['Author'] == author:
                similar_author_books.append(record['Title'])
        print(similar_author_books)

