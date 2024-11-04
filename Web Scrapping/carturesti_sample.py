from bs4 import BeautifulSoup
import requests

URL = 'https://carturesti.ro/carte/the-justice-of-kings-919610552?p=2'
source = requests.get(URL).text

soup = BeautifulSoup(source, 'lxml')


main_page = soup.find('div', class_='col-md-7')

title = main_page.find('div', class_='titlesContainer').h1.text.strip()
print(f"Book Title: {title}")

author = main_page.find('div', class_='autorProdus').a.text.strip()
print(f"Book Author: {author}")

price = main_page.find('div', class_='col-sm-6').text.strip()
print(f"Book Price: {price}")

availability = main_page.find('span', class_='stocText').text.strip()
print(f"Book Availability: {availability}")
