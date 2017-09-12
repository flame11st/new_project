from django.contrib import admin

# Register your models here.
from .models import Point, Icon, Photo, Type

admin.site.register(Point)
admin.site.register(Icon)
admin.site.register(Photo)
admin.site.register(Type)
