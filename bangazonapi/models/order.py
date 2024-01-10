from django.db import models
from .user import User
from .order_category import OrderCategory

class Order(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  order_name = models.CharField(max_length=100)
  customer_phone = models.CharField(max_length=15)
  customer_email = models.CharField(max_length=55)
  order_type = models.ForeignKey(OrderCategory, on_delete=models.CASCADE)
  timestamp = models.DateTimeField(max_length=100)
  order_total = models.DecimalField(max_digits=7, decimal_places=2)
  date = models.DateField(max_length=55)
  payment_type = models.CharField(max_length=55)
  order_status = models.CharField(max_length=55)
  is_closed = models.BooleanField()
  
  