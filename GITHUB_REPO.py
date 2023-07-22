from bs4 import BeautifulSoup
import requests

url = 'https://github.com/ahmedtaha89?tab=repositories'
page = requests.get(url)
soup = BeautifulSoup (page.text,'html.parser')
ul = soup.find_all('div',class_='Layout-main')

# print(ul)
for t in ul:
    title = t.find_all('a')
    print(title)