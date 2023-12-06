from django.contrib import admin
from todolist.models import Todolist


class TodolistAdmin(admin.ModelAdmin):
    list_display = ['name', 'value', 'datetime_field', 'comments']


admin.site.register(Todolist, TodolistAdmin)
