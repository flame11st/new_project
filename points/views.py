from django.shortcuts import get_object_or_404, render
import ast
from django.http import HttpResponse
from .models import Point
# Create your views here.


def index(request):
    latest_point_list = list(Point.objects.order_by('create_time')[:10:-1])
    context = {'latest_point_list': latest_point_list}
    return render(request, 'points/index.html', context)


def detail(request, point_id):
    point = get_object_or_404(Point, pk=point_id)
    geojson = ast.literal_eval(open('.'+point.coordinate.url, 'r' ).read())
    coord = geojson['features'][0]['geometry']['coordinates']
    return render(request, 'points/detail.html', {'point': point, 'coord': coord})