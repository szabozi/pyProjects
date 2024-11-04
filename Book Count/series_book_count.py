import gspread
from collections import defaultdict

# connecting to the service account json file
serviceAccount = gspread.service_account(filename="pythonSheets.json")

# connecting to the actual sheet
sheet = serviceAccount.open("Book Collection and Tracker")

# selecting the worksheet
worksheets = sheet.worksheet("Book-List")

# getting all the data: -> this is a list of dictionaries
# the keys will be the heathers, and the values will be the cell values
allData = worksheets.get_all_records()

# Storing the counts of each Series
series_counts = defaultdict(int)

# Iterate through all the data and count the occurrences of each series
for data in allData:
    series_name = data["Series"]
    series_counts[series_name] += 1

# Sorting the dictionary by values in descending order
sorted_series_counts = {k: v for k, v in sorted(series_counts.items(), key=lambda item: item[1], reverse=True)}

# Printing the counts of each unique series in descending order
for series, count in sorted_series_counts.items():
    if count > 1:
        print(f"Series: {series} --- Books: {count}")
