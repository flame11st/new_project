from django.db import models

# Create your models here.


class Point(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    picture_url = models.CharField(max_length=200)

    def __str__(self):
        return self.name+' (id: %s)'% (self.id)
