from django.db import models


class Route(models.Model):
    title = models.CharField(max_length=100)
#    edges = {}
    description = models.TextField(default='')

class Edge(models.Model):
    points = {}
    points[1] = models.ForeignKey('points.Point', on_delete=models.CASCADE)
    points[2] = models.ForeignKey( 'points.Point', on_delete=models.CASCADE)