from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']


class CustomLoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class SearchForm(forms.Form):
    search_term = forms.CharField(max_length=255)


class OrderForm(forms.Form):
    email = forms.EmailField()
    phone = forms.CharField()
    fullname = forms.CharField()
    region = forms.CharField()
    city = forms.CharField()
    price = forms.CharField()
    buying_method = forms.CharField()
    payment_method = forms.ChoiceField(choices=[('card', 'Карткою'), ('cash', 'Готівкою'), ('paypal', 'PayPal')], label="Спосіб оплати")
    goods = forms.CharField()