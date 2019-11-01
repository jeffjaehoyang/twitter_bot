from bs4 import BeautifulSoup
import requests, re, string

URL = "http://www.gutenberg.org/files/11224/11224-h/11224-h.htm"

#use BeautifulSoup to extract content we want from an e-book from a gutenberg project
def fetch_text(url):
	source = requests.get(url).text
	soup = BeautifulSoup(source, 'lxml')
	text_content = ''
	for el in soup.select('p'):
		text_content += el.text 
	return text_content

#text clean-up process
def text_cleanup(text):
	text = re.sub(r'\[.*?\]', '',text)
	text = re.sub(r'[^\w\d.\s]+', '', text)
	text = re.sub(r'\w*\d\w*', '', text)
	return text

output_file_write = open('gutenberg.txt', 'w')
output_file_write.write(text_cleanup(fetch_text(URL)))
output_file_write.close()

