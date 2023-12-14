from django.urls import path
from .views import *

urlpatterns = [
    # path('home/', home, name='home'),
    # path('tests/', testing, name='tests'),
    # path('protected_url/', protected_url, name='protected_url'),
    path('cart/', cart, name='cart'),
    path('order', order, name='order'),
    path('goods/search', search_view, name='search'),
    path('goods/item', show_item, name='show_item'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('goods/', show_goods, name='goods'),
    path('', default_page, name='default_page')
]