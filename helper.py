import requests
from bs4 import BeautifulSoup

URL = 'https://leagueoflegends.fandom.com/wiki/List_of_champions'
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

def champion_names():
    '''Returns a list of all of the champion names in League of Legends
    Indexes match the champion release years in the release_year() list below'''
    
    table = soup.find('table', {'class': 'article-table'})
    body = table.find('tbody')
    rows = body.find_all('tr')

    names = []

    for row in rows:
        td = row.find('td')
        if td:
            value = td.get('data-sort-value')
            if value:
                names.append(value)

    return names


def release_year():
    '''Returns a list of years in which the champions were released. 
    Indexes match the champion names in the champion_names() list above'''

    table = soup.find('table', {'class': 'article-table'})
    body = table.find('tbody')
    rows = body.find_all('tr')

    years = []

    for row in rows:
        tds = row.find_all('td')
        for index, td in enumerate(tds):
            if index == 2:
                text = td.text[:4]
                years.append(int(text))

    return years