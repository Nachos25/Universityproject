from django.urls import path
from .views import register, login_view, logout_view, default_page, home, show_goods, testing, show_item, proteected_url

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/', home, name='home'),
    path('goods', show_goods, name='goods'),
    path('goods/item', show_item, name='show_item'),
    path('tests/', testing, name='tests'),
    path('protected_url/', proteected_url, name='proteected_url'),
    path('', default_page, name='default_page')
]