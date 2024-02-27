from bs4 import BeautifulSoup
import requests

page = requests.get("https://en.wikipedia.org/wiki/Abraham_Lincoln") 
soup = BeautifulSoup(page.content, 'html.parser')
 
all_links = soup.find_all('a')

for link in all_links:
    print(link.get_text(), link.attrs.get('href'))
