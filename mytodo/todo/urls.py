from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("login/home", views.Home_Page, name="Welcome"),
    path("register/", views.register, name="Register"),
]
