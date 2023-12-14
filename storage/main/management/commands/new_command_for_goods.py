from django.core.management.base import BaseCommand
from main.models import Goods, Categories
from fake_useragent import UserAgent
import requests
import time
import random


link = "https://jabko.ua/"
ua = UserAgent().random
headers = {"User-Agent": ua}


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Indicates the number of users to be created')
        parser.add_argument('-sf', '--category', type=int, help='Define a username prefix', )

    def handle(self, *args, **options):
        count = options['count']
        category_id = options['category']
        skipped_link = ["apple-airpods/naushniki-apple-airpods/airpods-with-wireless-charging-case"]
        category = Categories.objects.get(id=category_id)
        category_part_of_link = category.link_to_category.split('text=')[-1]
        href = 'http://127.0.0.1:8000/api/get_goods_info?text=' + str(category_part_of_link)
        print(href)
        information = requests.get(href, headers=headers).json()
        for info in information:
            link_for_getting = info['url'].split('text=')[-1]
            if count > 1:
                count-=1
                info_about_good = requests.get('http://127.0.0.1:8000/api/get_good_info?text=' + str(link_for_getting), headers=headers).json()
                existing_product = Goods.objects.filter(good_name=info['name']).first()
                if existing_product:
                    category.goods.add(existing_product)
                else:
                    try:
                        good = Goods(good_name=info['name'], price=info['price'], currency=info['priceCurrency'],
                                         image=info['image'], link_to_good=info['url'], info_about_good=info_about_good)
                        good.save()
                        category.goods.add(good)
                    except KeyError:
                        good = Goods(good_name=info['name'], price="Тільки по попередньому замовленню",
                                         currency=info['priceCurrency'],
                                         image=info['image'], link_to_good=info['url'], info_about_good=info_about_good)
                        good.save()
                        category.goods.add(good)
                    self.stdout.write(self.style.SUCCESS(f'Data with {info["name"]} loaded successfully'))
            else:
                break
            time.sleep(random.randint(30, 60))
        self.stdout.write(self.style.SUCCESS(f'Data with {category_part_of_link} loaded successfully'))