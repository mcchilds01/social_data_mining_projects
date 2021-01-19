import csv
import requests
from bs4 import BeautifulSoup

headers = {'user-agent' : <USER-AGENT>,
 'from': <FROM INFO>}

rows = []

url = 'https://www.wikipedia.org/wiki/Category:Women_computer_scientists'

def scrapePage(url: str):
    page = requests.get(url, headers=headers) 
    page_content = page.content
    soup = BeautifulSoup(page_content, 'html.parser')
    content = soup.find('div', class_="mw-category")
    page_goupings = content.find_all('div', class_='mw-category-group')

    for grouping in page_goupings:
        names_list = grouping.find('ul')
        category = grouping.find('h3').get_text()
        alphabetical_names = names_list.find_all('li')

        for alphabetical_name in alphabetical_names:
            name = alphabetical_name.text
            anchortag = alphabetical_name.find('a', href=True)
            link = anchortag['href']
            letter_name = category
            row = {
                'name': name,
                'link': link,
                'letter_name':letter_name
            }
            rows.append(row)

scrapePage(url)

with open('women_computer_scientists.csv', 'w') as f:
    fieldnames = ['name', 'link', 'letter_name']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for row in rows:
        writer.writerow(row)
