import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL for the main fiction section page
base_url = "https://carturesti.ro/raft/fictiune-1181177"

# List to store book titles
titles = []

# Send a request to the main page and parse it
response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Locate and extract all book title elements based on the structure you provided
book_containers = soup.find_all('div', class_='cartu-grid-tile')

for book in book_containers:
    title_element = book.find('h5', class_='md-title')
    if title_element:
        title = title_element.get_text(strip=True)
        titles.append(title)

# Save titles to a CSV file
titles_df = pd.DataFrame({'Title': titles})
titles_df.to_csv('carturesti_main_page_titles.csv', index=False)
print("Titles saved to carturesti_main_page_titles.csv")
