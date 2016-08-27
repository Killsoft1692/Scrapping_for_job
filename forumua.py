# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import urllib

#driver = webdriver.Firefox()
#driver.get('http://forumua.org/forum/тематические-разделы/работа-и-трудоустройство/разовые-услуги-требуются')
html = urllib.urlopen('http://forumua.org/forum/тематические-разделы/работа-и-трудоустройство/разовые-услуги-требуются') 
soup = BeautifulSoup(html,'lxml')
for tag in soup.find_all("td", class_="cell-topic js-cell-topic"):
	disc = tag.text
	if u'закрыта' in disc:
		continue
	else:
		print disc.strip()
	#print tag.attrs['href']
		href = tag.find('a', class_='topic-title js-topic-title')
		try:
			print href.attrs['href']
		except:
			print 'Not found'
#for tag in soup.find_all('div'):
#	print tag