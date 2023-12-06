from django.core.management.base import BaseCommand
from main.models import Categories
from fake_useragent import UserAgent
import requests

ua = UserAgent().random
headers = {"User-Agent": ua}


class Command(BaseCommand):
    help = 'Load categories into the database'


    def handle(self, *args, **options):
        information = requests.get('http://127.0.0.1:8000/api/get_categoties', headers=headers).json()
        for category_name, category_info in information.items():
            Categories(category=category_name, link_to_category=category_info['href'], image=category_info['image']).save()
            self.stdout.write(self.style.SUCCESS(f'Data with {category_name} loaded successfully'))
