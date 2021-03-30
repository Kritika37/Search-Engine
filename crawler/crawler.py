
#creating a simple web crawler
import requests
from bs4 import BeautifulSoup


start_url = 'https://stackoverflow.com/'

def crawl(url):
	print('Crawl("%s")' % url)

	response = requests.get(start_url)
	content = BeautifulSoup(response.text,'lxml')

	links = content.findAll('a')
	description = content.findAll('p')


	for link in links:
		try:
			pass
		except KeyError:
			pass

crawl(start_url)