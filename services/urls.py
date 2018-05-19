from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name="login"),
    path('home/', views.home, name="home"),
    path('profile/', views.profile, name="profile"),
    path('register/', views.register, name="register"),
    path('loginuser/', views.login, name="validate"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
]
