from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('home/', views.home, name="home"),

    path('register/', views.register, name="register"),
    path('loginuser/', views.validate_user, name="validate"),
]
