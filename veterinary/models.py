from django.db import models
from django.contrib.auth.models import User

# Create your models here
class Veterinary(models.Model):
    user = models.ForeignKey(User,on_delete =models.CASCADE)
    name = models.CharField(max_length = 30)
    email = models.CharField(max_length=30,unique=True)
    county = models.CharField(max_length=30)
    id_no = models.IntegerField(unique=True)
    phone_number = models.IntegerField(unique=True)


    def __str__(self):
        return self.name
   
  
