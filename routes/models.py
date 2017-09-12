from django.db import models

# Create your models here.


class Point(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)
    type = models.ForeignKey('Type',on_delete=models.SET_NULL, null=True)
    photo = models.ForeignKey('Photo',on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    importence = models.ForeignKey('Importence',on_delete=models.SET_NULL, null=True, blank = True)
    facebook = models.URLField(max_length=200, blank = True)
    wiki = models.URLField(max_length=200, blank = True)
    trip_advisor = models.URLField(max_length=200, blank = True)
    Coordinate = models.FileField(upload_to=None, max_length=100)

    def __str__(self):
        return self.title+' (id: %s)' % self.create_time


class Importence(models.Model):
    title = models.FloatField()

class Type(models.Model):
    title = models.CharField(max_length=100)
    icon = models.ForeignKey('Icon',on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Icon(models.Model):
    title = models.CharField(max_length=100)
    image = models.URLField(max_length=200)

    def __str__(self):
        return self.title


class Photo(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    copyright = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title