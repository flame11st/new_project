from django.shortcuts import get_object_or_404, render
import ast

from .models import Route, Edge


def index(request):
#    countries = list(Country.objects.order_by('title'))
#    cities = list( City.objects.order_by('title'))
#    importences = list(Importance.objects.order_by('title'))
    all_routes_list = list(Route.objects.all()[:12:-1])
    context = {'all_routes_list': all_routes_list}
    return render(request, 'routes/index.html', context)


def detail(request, route_id):
    route = get_object_or_404(Route, pk=route_id)
#    geojson = ast.literal_eval(open('.'+point.coordinate.url, 'r' ).read())
#    coord = geojson['features'][0]['geometry']['coordinates']

    context = {'route': route}
    return render(request, 'routes/detail.html', context)