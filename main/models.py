from django.db import models

class ShopGoods(models.Model):
    product_name = models.CharField(max_length=500, unique=True)
    price = models.CharField(max_length=50)
    currency = models.CharField(max_length=10)
    image = models.CharField(max_length=300)
    link_to_product = models.CharField(max_length=700)
    info_about_product = models.JSONField()


class Categories(models.Model):
    category = models.CharField(max_length=500)
    link_to_category = models.CharField(max_length=760)
    image = models.CharField(max_length=800)
    goods = models.ManyToManyField(ShopGoods)


class Orders(models.Model):
    email = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    fullname = models.CharField(max_length=500)
    region = models.CharField(max_length=500)
    city = models.CharField(max_length=500)
    price = models.CharField(max_length=20, default=None)
    buying_method = models.CharField(max_length=20, default="default")
    payment_method = models.CharField(max_length=500)
    goods = models.CharField(max_length=100000)