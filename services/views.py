from django.http import HttpResponse
from django.shortcuts import render, redirect

# Models
from django.contrib.auth.models import User
from services.models import *

def index(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, "index.html")

def login(request):
    return render(request, "login.html")

def home(request):
    if not request.user.is_authenticated:
        return redirect('index')
    return render(request, "home.html")

def profile(request):
    if not request.user.is_authenticated:
        return redirect('index')
    user = request.user
    my_user = MyUser.objects.get(user_django=user)
    my_user_id = my_user.id
    post = Post.objects.filter(user_id=my_user_id)
    number_followers = Follow.objects.filter(user_to_id=my_user_id).count()
    number_victims = Follow.objects.filter(user_from_id=my_user_id).count()
    print(user.username)
    context = dict(
        username=user.username,
        post=post,
        number_followers=number_followers,
        number_victims=number_victims,
        my_user=my_user
    )
    return render(request, "profile.html", context)

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
        return redirect('login')
    return redirect('index')


def validate_user(request):
    return redirect('home')
