from django.urls import path
from .views import *

urlpatterns = [
    # path('home/', home, name='home'),
    # path('tests/', testing, name='tests'),
    # path('protected_url/', protected_url, name='protected_url'),
    # path('cart/', show_cart, name='show_cart'),
    path('goods/item', show_item, name='show_item'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('goods', show_goods, name='goods'),
    path('', default_page, name='default_page'),
    path('cart/', cart, name='cart')
]