import bs4
import requests
from requests import Session
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as BS
import json

ua = UserAgent().random
headers = {"User-Agent": ua}
link = "http://127.0.0.1:8000/api/get_goods_info?text=" + 'apple'
link = "https://jabko.ua/"

def get_data(text):
    content = requests.get(url=link + text, headers=headers).text
    soup = BS(content, 'lxml')
    try:
        text_info = soup.find_all("script")[-13].text
        try:
            new_price = soup.find('span', class_='price-new__uah').get_text().replace(' грн', '')
        except:
            pass
        json_string_without_comments = '\n'.join(
            line for line in text_info.split('\n') if not line.strip().startswith('//'))
        data = json.loads(json_string_without_comments)
    except json.decoder.JSONDecodeError:
        text_info = soup.find_all("script")[-14].text
        try:
            new_price = soup.find('span', class_='price-new__uah').get_text().replace(' грн', '')
        except:
            pass
        json_string_without_comments = '\n'.join(
            line for line in text_info.split('\n') if not line.strip().startswith('//'))
        data = json.loads(json_string_without_comments)

    name = soup.find('h1', class_='product-info__title_m').text
    # images_list = soup.find('section', class_='product').find_all('img', attrs={'title': name})
    images_list = soup.find('section', class_='product').find('div', class_='product-img__slider').find_all('img')
    for i in range(len(images_list)):
        item = images_list[i]
        images_list[i] = item.get('src')
    count = len(images_list) / 2
    big_images = images_list[:int(count)]
    small_images = images_list[int(count):]
    data['big_images'] = big_images
    data['name'] = name.strip()
    data['small_images'] = small_images
    if 'price' in data['offers']:
        price = data['offers']['price']
        data['new_price'] = new_price
        data['offers']['price'] = '{:,.0f}'.format(float(price)).replace(',', ' ')
    return data

print(get_data("gadzheti-i-drugoe/playstation/nintendo-switch/portativnaja-igrovaja-pristavka-nintendo-switch-oled-with-white-joy-con--045496453435-"))

