from django.contrib import admin
from .models import Profile, Todo


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "date_of_birth",
    ]


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "Date_Created",
    ]

    class meta:
        ordering = "-Date_Created"
