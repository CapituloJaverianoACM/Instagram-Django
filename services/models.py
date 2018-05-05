from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class MyUser(models.Model):
    photo = models.CharField(null=True, max_length=200)
    description = models.CharField(null=True, max_length=200)
    birth_date = models.DateField(null=True)
    user_django = models.OneToOneField(User, on_delete=models.CASCADE)


class Follow(models.Model):
    user_from = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='user_from')
    user_to = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='user_to')


class Post(models.Model):
    photo = models.CharField(max_length=200)
    description = models.CharField(null=True, max_length=200)
    date = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Like(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
