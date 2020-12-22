import requests
from bs4 import BeautifulSoup as BS

r = requests.get('https://www.hltv.org/ranking/teams/2020/november/16')
html = BS(r.content, 'html.parser')

for el in html.select('.lent-block'):
	title = el.select('.lent-title > a')
	print (title[0])