from django.http import HttpResponse
from django.shortcuts import render, redirect

# Models
from django.contrib.auth.models import User
from services.models import MyUser

def index(request):
    return render(request, "index.html")

def login(request):
    return render(request, "login.html")

def home(request):
    return render(request, "home.html")

def register(request):
    if request.method == 'POST':
        post_form_data = request.POST
        data = dict(
            username=post_form_data.get('username'),
            email=post_form_data.get('email'),
            first_name=post_form_data.get('name'),
            password=post_form_data.get('password')
        )
        user = User.objects.create_user(**data)
        my_user = MyUser.objects.create(user_django=user)
        return redirect('home')
    return redirect('index')


def validate_user(request):
    return redirect('home')
