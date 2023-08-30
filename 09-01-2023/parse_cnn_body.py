from bs4 import BeautifulSoup
import requests

# A randomly selected CNN article from the day I wrote this script.
page = requests.get("https://www.cnn.com/2023/08/30/business/san-francisco-union-square-retail-closures/index.html")

soup = BeautifulSoup(page.content, 'html.parser')
individual_p_tags = soup.select('.article__content p')  # CNN's content sits in p tags under a div with this class
texts = [tag.text.strip() for tag in individual_p_tags]
a_text = '\n'.join(texts)

with open('09-01-2023/news_text_out/cnn_article.txt', 'w') as file:
    file.write(a_text)