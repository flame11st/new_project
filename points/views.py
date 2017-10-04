from django.shortcuts import get_object_or_404, render
import ast
from django.http import HttpResponse
from .models import Point, Country, City, Importance
# Create your views here.


def index(request):
    countries = list(Country.objects.order_by('title'))
    cities = list( City.objects.order_by('title'))
    importences = list(Importance.objects.order_by('title'))
    latest_point_list = list(Point.objects.order_by('create_time')[:12:-1])
    context = {'latest_point_list': latest_point_list, 'countries': countries, 'cities': cities, 'importences': importences}
    return render(request, 'points/index.html', context)


def detail(request, point_id):
    point = get_object_or_404(Point, pk=point_id)
    geojson = ast.literal_eval(open('.'+point.coordinate.url, 'r' ).read())
    coord = geojson['features'][0]['geometry']['coordinates']
    context = {'point': point, 'coord': coord}
    return render(request, 'points/detail.html', context)