from django.contrib import admin

# Register your models here.
from .models import Route, Edge
admin.site.register([
    Route,
    Edge,
    ])
