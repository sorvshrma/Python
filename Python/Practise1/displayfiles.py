import os,glob
import requests
import bs4

res = requests.get('https://hackernoon.com/building-a-web-scraper-from-start-to-finish-bb6b95388184')
#print(type(res))
#print(res.text)

#soup = bs4.BeautifulSoup(res.text,'html')

soup = bs4.BeautifulSoup(res.text,'html.parser')

hi = soup.select('title')
#print(hi)

print(hi[0].getText())