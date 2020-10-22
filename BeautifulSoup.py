from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import pandas as pd
import requests

url = "https://stepik.org/media/attachments/lesson/209723/5.html"
r = requests.get(url).content

soup = BeautifulSoup(r, 'html.parser')

table = []

table = soup.table.find_all('td')

summ = 0
for td in table:
    print(td.text)
    summ += int(td.text)

    #tds = tr.findAll('td')
    #for td in tds.findAll('td'):
      #  print('td')

print(summ)




#print(html)