from django.db import models
from SignIn.models import User
# Create your models here.

class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True) 

     