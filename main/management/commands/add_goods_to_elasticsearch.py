from django.core.management.base import BaseCommand
from main.models import Goods


class Command(BaseCommand):
    help = 'load goods to elasticsearch'

    def handle(self, *args, **options):
        pass
