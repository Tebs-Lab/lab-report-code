from bs4 import BeautifulSoup
import requests
import shutil

base_url = "https://en.wikipedia.org"
page = requests.get("https://en.wikipedia.org/wiki/Abraham_Lincoln") 
soup = BeautifulSoup(page.content, 'html.parser')
 
all_img_tags = soup.find_all('img')

img_count = 0
for img in all_img_tags:
    img_url = img.attrs.get('src')
    # Images on wikipedia have a few formats for the src value, which require special handling.
    if img_url.startswith('//'):
        absolute_url = f'https:{img_url}'
    else:
        absolute_url = base_url + img_url

    response = requests.get(absolute_url, stream=True)
    file_type = response.headers['content-type'].split('/')[-1] # kinda gross, but works.
    with open(f'09-01-2023/img_out/{img_count}.{file_type}', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    img_count += 1