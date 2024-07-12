from django.db import models


# Create your models here.
class Nauczyciel(models.Model):
    name = models.CharField(max_length=50)
    day = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    room_number = models.IntegerField()
