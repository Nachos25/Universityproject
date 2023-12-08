from django_elasticsearch_dsl import Document, Text
from django_elasticsearch_dsl.registries import registry
from .models import Goods


@registry.register_document
class GoodsDocument(Document):
    class Index:
        name = 'goods'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    class Django:
         model = Goods
         fields = [
             'good_name',
             'price',
             'currency',
             'image',
             'link_to_good',
         ]