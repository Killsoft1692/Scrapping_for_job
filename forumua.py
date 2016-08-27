# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib

html = urllib.urlopen('http://forumua.org/forum/тематические-разделы/работа-и-трудоустройство/разовые-услуги-требуются') 
soup = BeautifulSoup(html,'lxml')
for tag in soup.find_all("td", class_="cell-topic js-cell-topic"):
	disc = tag.text
	if u'закрыта' in disc:
		continue
	else:
		print disc.strip()
	
		href = tag.find('a', class_='topic-title js-topic-title')
	
		try:
			print href.attrs['href']
		except:
			print 'Not found'

