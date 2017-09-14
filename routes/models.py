from django.db import models

class Route(models.Model):
    title = models.CharField(max_length=100)
#    edges = {}
    description = models.TextField(default='')


class Edge(models.Model):
    title = models.CharField(max_length=100)
    point_1 = models.ForeignKey('points.Point', on_delete=models.CASCADE, default='')
    point_2 = models.ForeignKey('points.Point', on_delete=models.CASCADE, related_name='%(class)s_edges_point2', default='')
    description = models.TextField(default='')
    transports = models.ManyToManyField('Transport', default='')

    def __str__(self):
        return self.title


class Transport(models.Model):
    title = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='uploads/transports', width_field=100, height_field=100, max_length=100, default='')