from django.contrib import admin
from django.urls import path, include
from . import views
import django.contrib.auth.urls
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path("login/", views.user_login, name="login"),
    path("login/home", views.Home_Page, name="home"),
    # path("register/", views.register, name="Register"),
    path("", include("django.contrib.auth.urls")),
]
