from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

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
    context = dict(username=request.user.username)
    return render(request, "home.html", context)


def upload_photo(request):
    if not request.user.is_authenticated:
        return redirect('index')
    if request.method == 'GET':
        context = dict(username=request.user.username)
        return render(request, "upload.html", context)
    if request.method == 'POST':
        username = request.user.username
        my_user = request.user.myuser
        last_post = Post.objects.filter(user=my_user).last()
        if last_post:
            photo_id = last_post.id + 1
        else:
            photo_id = 1
        description = request.POST['description']
        photo = request.FILES['file']
        photo_name = username + '_photo_' + str(photo_id)
        fs = FileSystemStorage()
        url_photo = fs.save(photo_name, photo)
        path_photo = fs.url(url_photo)

        post = Post.objects.create(photo=path_photo, description=description, user=my_user)
        return redirect('profile')


def profile(request, username):
    if not request.user.is_authenticated:
        return redirect('index')

    context = dict()
    if username == request.user.username:
        user = request.user
    else:
        user = User.objects.get(username=username)
        is_follow = Follow.objects.filter(user_from=request.user.myuser, user_to=user.myuser).exists()
        context.update(is_follow=is_follow)

    my_user = MyUser.objects.get(user_django=user)
    my_user_id = my_user.id
    post = Post.objects.filter(user_id=my_user_id)
    number_followers = Follow.objects.filter(user_to_id=my_user_id).count()
    number_victims = Follow.objects.filter(user_from_id=my_user_id).count()
    context.update(
        username=request.user.username,
        current_username=user.username,
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


def search(request):
    username = request.POST['search_username']
    user = User.objects.get(username=username)
    if user:
        return redirect('profile', user.username)
    else:
        return redirect('profile', request.user.username)


def follow(request, begin, end):
    user_begin = User.objects.get(username=begin)
    user_end = User.objects.get(username=end)
    Follow.objects.create(user_from=user_begin.myuser, user_to=user_end.myuser)
    return redirect('profile', end)


def unfollow(request, begin, end):
    user_begin = User.objects.get(username=begin)
    user_end = User.objects.get(username=end)
    follow = Follow.objects.get(user_from=user_begin.myuser, user_to=user_end.myuser)
    follow.delete()
    return redirect('profile', end)
