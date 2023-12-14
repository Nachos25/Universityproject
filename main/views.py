from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, CustomLoginForm, SearchForm, OrderForm
from django.core.paginator import Paginator
from django.core.serializers import serialize
from django.contrib.auth.models import User
from main.documents import GoodsDocument
from .models import ShopGoods, Categories, Orders
from django.contrib import messages
from elasticsearch_dsl import Q
import json


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = email.split("@")[0]
            user = form.save(commit=False)
            user.username = username
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Користувач вже існує або\nпаролі не свівпадають')
    else:
        form = RegistrationForm()
    return render(request, 'registration/registration.html', {'forma': form})


def login_view(request):
    form = CustomLoginForm(request.POST)
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        try:
            username = User.objects.get(email=email).username
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Перевірте email і пароль')
        except User.DoesNotExist:
            messages.error(request, 'Користувача з даним email не знайдено')

    return render(request, 'registration/log-in.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')


def default_page(request):
    info = json.loads(serialize('json', Categories.objects.all()))
    return render(request, 'index.html', {'info': info})


def show_goods(request):
    text_param = request.GET.get('text', '')
    info = Categories.objects.get(link_to_category="goods?page=1&text=" + text_param)
    info_about_goods = info.goods.all()
    info = json.loads(serialize('json', info_about_goods))
    paginator = Paginator(info, 15)
    page = request.GET.get('page')
    items = paginator.get_page(page)
    return render(request, "category.html", {"info": items, 'searched': text_param})


def show_item(request):
    text_param = request.GET.get('text', '')
    info = ShopGoods.objects.get(link_to_product="/goods/item?text=" + text_param)
    info = json.loads(serialize('json', [info]))
    return render(request, 'item.html', {'info': info[0]})

def search_view(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            search_term = form.cleaned_data['search_term']
            if search_term == None:
                redirect('/')
            # text_param = request.GET.get('text', '')
            # q = Q('match_phrase', query="навушники apple", field='good_name')
            # q = Q('match_phrase', good_name=text_param)
            q = Q('prefix', product_name=search_term)
            search = GoodsDocument.search().query(q).extra(size=500).execute().to_dict()
            paginator = Paginator(search['hits']['hits'], 15)
            page = request.GET.get('page')
            items = paginator.get_page(page)
    else:
        search_term = request.GET.get('text', '')
        q = Q('prefix', product_name=search_term)
        search = GoodsDocument.search().query(q).extra(size=500).execute().to_dict()
        paginator = Paginator(search['hits']['hits'], 15)
        page = request.GET.get('page')
        items = paginator.get_page(page)
    return render(request, 'category.html', {'info': items, 'searched': search_term})


def cart(request):
    return render(request, 'cart.html', )

def order(request):
    text_param = request.GET.get('text', '')
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            fullname = form.cleaned_data['fullname']
            region = form.cleaned_data['region']
            city = form.cleaned_data['city']
            payment_method = form.cleaned_data['payment_method']
            goods = form.cleaned_data['goods']
            buying_method = form.cleaned_data['buying_method']
            price = form.cleaned_data['price']
            Orders(email=email, phone=phone, fullname=fullname, region=region, city=city, buying_method=buying_method, price=price, payment_method=payment_method, goods=goods).save()
            return redirect('/')
    else:
        form = OrderForm(request.POST)
    return render(request, 'order.html', {"text_param": text_param})
