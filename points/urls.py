from django.conf.urls import url

from . import views

app_name = 'points'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<point_id>[0-9]+)/$', views.detail, name='detail'),
]