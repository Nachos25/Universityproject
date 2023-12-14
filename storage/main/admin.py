from django.contrib import admin
from .models import Categories, Goods


class GoodsInline(admin.TabularInline):
    model = Categories.goods.through


@admin.register(Goods)
class CategoriesAdmin(admin.ModelAdmin):
    model = Goods
    inlines = [GoodsInline]


admin.site.register(Categories)

