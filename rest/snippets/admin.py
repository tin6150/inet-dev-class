from django.contrib import admin

# Register your models here.

## https://wsvincent.com/official-django-rest-framework-tutorial-beginners-guide/

# snippets/admin.py
from django.contrib import admin
from . models import Snippet

admin.site.register(Snippet)
