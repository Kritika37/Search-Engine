
#creating a simple web crawler
import requests
import json
from bs4 import BeautifulSoup


start_url = 'https://stackoverflow.com/'

def crawl(url,depth):

	response = requests.get(start_url)
	content = BeautifulSoup(response.text,'lxml')

	
	title = content.find('title').text
	description = content.find('p').text.strip().replace('\n', '')

	result = {
	      'url' : url,
	      'title' : title,
	      'description' : description
	}

	if depth == 0:
		return result

	try:
		links = content.findAll('a')
	except:
		return result

	for link in links:
		try:
			print('following url: "%s"' % link['href'])
		except KeyError:
			pass

	return result

result = crawl(start_url,1)
print(json.dumps(result,indent=2))