from django.db import models

# Create your models here.


class Recipe(models.Model):
    name= models.CharField(max_length=50)
    id= models.IntegerField
    Appetizers= models.CharField(max_length=100)
    image= models.ImageField(upload_to='photos')