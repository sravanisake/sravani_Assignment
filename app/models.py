from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class country(models.Model):
    username=models.ForeignKey(User, on_delete=models.CASCADE)
    countryname=models.CharField(max_length=100)
    countrylanguage=models.CharField(max_length=100)
    countryimage=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    countryfood=models.CharField(max_length=100)
    countrywonders=models.IntegerField()
    Descripition=models.CharField(max_length=250)


    def __str__(self):
        return self.countryname
