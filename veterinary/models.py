from django.db import models
from django.contrib.auth.models import User

# Create your models here
class Veterinary(models.Model):
    user = models.ForeignKey(User,on_delete =models.CASCADE)
    name = models.CharField(max_length = 20)
    email = models.CharField(max_length=20)
    id_no = models.IntegerField(default = 0)
    phone_number = models.IntegerField(default = 0)
    # county = models.CharField(max_length=255)

    def __str__(self):
        return self.name
   
  
