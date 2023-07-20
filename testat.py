from bs4 import BeautifulSoup
import requests
import csv
from itertools import zip_longest
url ='https://admin-area.testat-app.com/tests/all-tests'
page = requests.get(url)
soup = BeautifulSoup(page.text,'html.parser')
Question_one = soup.find('tbody')  
print(soup)