from bs4 import BeautifulSoup
import requests

# A randomly selected BBC article from the day I wrote this script.
page = requests.get("https://www.bbc.com/sport/football/66662060")
soup = BeautifulSoup(page.content, 'html.parser')

# BBC wraps the main body in a div with this class, but uses p's for the text
individual_p_tags = soup.select('.story-body p')
texts = [tag.text for tag in individual_p_tags]
a_text = '\n'.join(texts)

with open('09-01-2023/news_text_out/bbc_article.txt', 'w') as file:
    file.write(a_text)

