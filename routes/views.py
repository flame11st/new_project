from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
#from .models import Point
# Create your views here.


#def index(request):
#    latest_route_list = list(Route.objects.order_by('create_time')[:10:-1])
#    context = {'latest_point_list': latest_point_list}
#    return render(request, 'routes/index.html', context)

def index(request):
    return HttpResponse("You're looking at routes")
