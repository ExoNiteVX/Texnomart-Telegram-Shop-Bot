import json
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os


def tilvizr(category):
    tilvizr_data = []
    load_dotenv()

    URL = os.getenv('URL')
    HOST = os.getenv('HOST')
    HEADERS = {
       'user-agent': 'MOZILLA'
        }

    html = requests.get(URL + category, headers=HEADERS).text
    soup = BeautifulSoup(html, "html.parser")

    blocks = soup.find_all('div', class_="col-3")

    for block in blocks:
        images_link = block.find('a', class_="product-link")
        rasm = images_link.find('img').get('data-src')
        title = block.find('h2').get_text()
        credit_price = block.find('div', class_='installment-price').get_text(strip=True)
        price = block.find('div', class_='product-price__current').get_text(strip=True)

        tilvizr_data.append({
        'rasmi': rasm,
        'nomi': title,
        'kreditga': credit_price,
        'narxi': price,
         })
    return tilvizr_data

tilvizr('katalog/televizory/')