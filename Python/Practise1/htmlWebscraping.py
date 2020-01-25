from bs4 import BeautifulSoup
import  requests

url = 'https://weather.com/'

source = requests.get(url)
soup = BeautifulSoup(source.text, 'html.parser')
title = soup.find('title')

print(title)

header_list = soup.find('ul',class_="styles__root__1ftiD styles__overflowNav__lGuSb")
weather = header_list.find_all('li')

#print(weather[0])

for i in weather[:4]:
    print(i)

print(weather[1].find('span').get_text())

listall = [w.find('span').get_text() for w in weather]

print(listall)




