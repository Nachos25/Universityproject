from django.contrib import admin
from .models import Categories, ShopGoods, Orders


class GoodsInline(admin.TabularInline):
    model = Categories.goods.through


@admin.register(ShopGoods)
class CategoriesAdmin(admin.ModelAdmin):
    model = ShopGoods
    inlines = [GoodsInline]


admin.site.register(Categories)
admin.site.register(Orders)


