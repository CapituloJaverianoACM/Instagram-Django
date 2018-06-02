from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name="login"),
    path('home/', views.home, name="home"),
    path('like/', views.like, name="like"),
    path('dislike/', views.dislike, name="dislike"),
    path('comment/<int:post_id>', views.comment, name="comment"),
    path('profile/<str:username>', views.profile, name="profile"),
    path('register/', views.register, name="register"),
    path('loginuser/', views.login, name="validate"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('upload/', views.upload_photo, name="upload"),
    path('search/', views.search, name="search"),
    path('follow/<str:begin>/<str:end>', views.follow, name="follow"),
    path('unfollow/<str:begin>/<str:end>', views.unfollow, name="unfollow"),
]
