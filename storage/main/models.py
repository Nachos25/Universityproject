from django.db import models


class Goods(models.Model):
    good_name = models.CharField(max_length=500, unique=True)
    price = models.CharField(max_length=50)
    currency = models.CharField(max_length=10)
    image = models.CharField(max_length=300)
    link_to_good = models.CharField(max_length=700)
    info_about_good = models.JSONField()


class Categories(models.Model):
    category = models.CharField(max_length=500)
    link_to_category = models.CharField(max_length=760)
    image = models.CharField(max_length=800)
    goods = models.ManyToManyField(Goods)


