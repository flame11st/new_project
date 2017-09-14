from django.contrib import admin

# Register your models here.
from .models import Point, Photo, Type, Importence, City, Country

admin.site.register([
    Point,
    Photo,
    Type,
    Country,
    City,
    Importence
    ])
