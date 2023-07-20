from bs4 import BeautifulSoup
import requests
import csv
from itertools import zip_longest
url ='https://ar.onlinesoccermanager.com/League/Standings'
page = requests.get(url)
soup = BeautifulSoup(page.text,'html.parser')
tabel_1 = soup.find('div',class_='tab-content')
print(tabel_1)
