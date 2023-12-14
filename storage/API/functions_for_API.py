import requests
from bs4 import BeautifulSoup as BS
import json
import os
from fake_useragent import UserAgent

ua = UserAgent().random
headers = {"User-Agent": ua}
link = "https://jabko.ua/"


def create_soup(request):
    soup = BS(request, 'lxml')
    return soup


def parser_for_categoties():
    request = requests.get(url=link, headers=headers).text
    main_div = create_soup(request).find("div", class_="menu-container")
    the_first_ul = main_div.find("ul", class_="mega-menu main inline-menu").find_all("a")
    the_second_ul = main_div.find_all("ul", class_="mega-menu default prelast-level")
    file_path = os.path.join(os.path.dirname(__file__), '..', 'main/static/main/json/', 'info.json')
    with open(file_path, 'r') as file:
        data = json.load(file)
        images = data['images']
    json_info = {}
    count = 0
    print(the_first_ul)
    print(the_second_ul)
    for item, item2 in zip(the_first_ul, the_second_ul):
        json_info[item.text.strip()] = {'href': item['href'], 'image': images[count], "items": {}}
        count += 1
        span_items = item2.find_all("a", class_="mega-menu--link")
        for new_item in span_items:
            json_info[item.text.strip()]['items'][new_item.text.strip()] = new_item['href']
    # list_with_links = ['apple', 'apple-airpods', 'dyson', 'b-u-apple', 'sony-playstation', 'gopro', 'smart-chasi', 'naushniki-i-audio', 'smartfoni', 'plansheti', 'gaming', 'kompjuteri-i-noutbuki', 'tehnika-dlja-doma', 'krasota-i-zdorove', 'gadzheti-i-drugoe', 'aksessuari', 'zaryadni-stanciyi', 'televizori']
    for name, information in json_info.items():
        href = information['href'].split('/')[-2]
        information['href'] = 'goods?page=1&text=' + href
    return json_info


def parser_for_goods(text):
    request = requests.get(url=link + text, headers=headers).text
    soup = create_soup(request).find_all("script")
    try:
        text_info = soup[20].text
        json_info = json.loads(text_info)["Offers"]
    except KeyError:
        text_info = soup[19].text
        json_info = json.loads(text_info)["Offers"]
    except json.decoder.JSONDecodeError:
        try:
            text_info = soup[-22].text
            print(text_info)
            json_info = json.loads(text_info)["Offers"]
        except KeyError:
            text_info = soup[-21].text
            json_info = json.loads(text_info)["Offers"]
    for item in json_info:
        url = item['url']
        image = item['image']
        item['image'] = image.replace("cachewebp", "cache").replace("400x400.webp", "400x400.jpg.webp")
        item['url'] = url.replace('https://jabko.ua/', '/goods/item?text=')
        if 'price' in item:
            price = item['price']
            item['price'] = '{:,.0f}'.format(float(price)).replace(',', ' ')
    return json_info


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
    print(data['offers'])
    if 'price' in data['offers']:
        try:
            price = data['offers'].get('price')
            data['new_price'] = new_price
            data['offers']['price'] = '{:,.0f}'.format(float(price)).replace(',', ' ')
        except UnboundLocalError:
            data['new_price'] = "Тільки по попередньому замовленню"
            data['offers']['prce'] = 'Тільки по попередньому замовленню'
    return data
