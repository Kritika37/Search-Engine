
#creating a simple web crawler
import requests
import json
from bs4 import BeautifulSoup


start_url = 'https://stackoverflow.com/'

def crawl(url):

	response = requests.get(start_url)
	content = BeautifulSoup(response.text,'lxml')

	links = content.findAll('a')
	title = content.find('title').text
	description = content.find('p').text 


	for link in links:
		try:
			pass
		except KeyError:
			pass

	return {
	      'url' : url,
	      'title' : title,
	      'description' : description
	}

result = crawl(start_url)
print(json.dumps(result,indent=2))