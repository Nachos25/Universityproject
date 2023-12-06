from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, CustomLoginForm
from django.core.paginator import Paginator
from django.core.cache import cache
from django.contrib.auth.models import User
import requests
from .models import Goods, Categories
from django.http import JsonResponse
from fake_useragent import UserAgent
from django.contrib import messages


ua = UserAgent().random
headers = {"User-Agent": ua}


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = email.split('@')[0]
            user = form.save(commit=False)
            user.username = username
            user = form.save()
            login(request, user)
            return redirect('/goods?page=1&text=mac')
        else:
            messages.error(request, 'Користувач вже існує або\nпаролі не свівпадають')
    else:
        form = RegistrationForm()

    return render(request, 'registration/registration.html', {'form': form})


# @require_POST
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
                return redirect('/goods?page=1&text=mac')
            else:
                messages.error(request, 'Перевірте email і пароль')
        except User.DoesNotExist:
            messages.error(request, 'Користувача з даним email не знайдено')

    return render(request, 'registration/log-in.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/goods?page=1&text=mac')


def home(request):
    return render(request, 'home.html')


def default_page(request):
    info = requests.get('http://127.0.0.1:8000/api/get_categoties', headers=headers).json()
    print(info)
    return render(request, 'index.html', {"info": info})


def show_goods(request):
    text_param = request.GET.get('text', '')
    cache_for_app = cache.get(f'info_{text_param}')
    if cache_for_app is None:
        info = requests.get(f"http://127.0.0.1:8000/api/get_goods_info?text={text_param}", headers=headers).json()
        cache.set(f'info_{text_param}', info, 60*60)
        paginator = Paginator(info, 15)
    else:
        paginator = Paginator(cache_for_app, 15)
    page = request.GET.get('page')
    items = paginator.get_page(page)
    return render(request, "category.html", {"information": items, 'text': text_param})


def show_item(request):
    text_param = request.GET.get('text', '')
    cache_for_app = cache.get(text_param)
    print(text_param)
    if cache_for_app is None:
        info = requests.get(f"http://127.0.0.1:8000/api/get_good_info?text={text_param}", headers=headers).json()
        cache.set(text_param, info, 60*60)
    else:
        info = cache_for_app
    return render(request, 'item.html', {'info': info})



def testing(request):
    text_param = request.GET.get('text', '')
    response = {'text_param': text_param}
    return JsonResponse(response)


@login_required()
def protected_url(request):
    return render(request, 'protected.html')


@login_required()
def show_cart(request):
    return render(request, 'cart.html')