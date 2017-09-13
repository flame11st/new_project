from django.contrib import admin

# Register your models here.
from .models import Point, Icon, Photo, Type, Importence, City, Country

admin.site.register([
    Point,
    Icon,
    Photo,
    Type,
    Country,
    City,
    ])
