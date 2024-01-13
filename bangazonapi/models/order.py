from django.db import models
from .user import User

class Order(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  phone = models.CharField(max_length=55)
  email = models.CharField(max_length=55)
  type = models.CharField(max_length=55)
  open = models.BooleanField()
  
  