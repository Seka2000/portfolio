import requests
from bs4 import BeautifulSoup
asd = input('ссылку : ')
url = asd
response = requests.get(url)
soup = BeautifulSoup(response.text, 'div')

print(soup)