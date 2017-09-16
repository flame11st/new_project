from django.db import models


class Route(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=400)
    author = models.CharField(max_length=100)
    cost = models.FloatField()
    duration = models.CharField(max_length=100)
    distance = 0.0
    edge_1 = models.ForeignKey('Edge', on_delete=models.CASCADE)
    edge_2 = models.ForeignKey('Edge', on_delete=models.CASCADE, related_name='%(class)s_route_edge2')
    edge_3 = models.ForeignKey('Edge', on_delete=models.CASCADE, related_name='%(class)s_route_edge3')
    edge_4 = models.ForeignKey('Edge', on_delete=models.CASCADE, related_name='%(class)s_route_edge4', blank=True)
    edge_5 = models.ForeignKey('Edge', on_delete=models.CASCADE, related_name='%(class)s_route_edge5', blank=True)
    edge_6 = models.ForeignKey('Edge', on_delete=models.CASCADE, related_name='%(class)s_route_edge6', blank=True)
    edge_7 = models.ForeignKey('Edge', on_delete=models.CASCADE, related_name='%(class)s_route_edge7', blank=True)
    edge_8 = models.ForeignKey('Edge', on_delete=models.CASCADE, related_name='%(class)s_route_edge8', blank=True)
    edge_9 = models.ForeignKey('Edge', on_delete=models.CASCADE, related_name='%(class)s_route_edge9', blank=True)
    edge_10 = models.ForeignKey('Edge', on_delete=models.CASCADE, related_name='%(class)s_route_edge10', blank=True)

    def __str__(self):
        self.distance = self.edge_1.distance+self.edge_2.distance+self.edge_3.distance
        self.description = self.edge_1.description+'\n\n'+self.edge_2.description+'\n\n'+self.edge_3.description
        return self.title


class Edge(models.Model):
    point_1 = models.ForeignKey('points.Point', on_delete=models.CASCADE, default='')
    point_2 = models.ForeignKey('points.Point', on_delete=models.CASCADE, related_name='%(class)s_edges_point2', default='')
    description = models.TextField(default='')
    transports = models.ManyToManyField('Transport', default='')
    distance = models.FloatField(default=0)

    def __str__(self):
        self.title = self.point_1.title+"  ==>  "+self.point_2.title
        return self.title


class Transport(models.Model):
    title = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='uploads/transports', max_length=100, default='')

    def __str__(self):
        return self.title
