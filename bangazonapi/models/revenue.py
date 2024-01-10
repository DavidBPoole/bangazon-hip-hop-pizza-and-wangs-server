from django.db import models
from .order import Order
from .payment_type import PaymentType

class Revenue(models.Model):
  order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
  total_revenue = models.DecimalField(max_digits=7, decimal_places=2)
  tip = models.DecimalField(max_digits=7, decimal_places=2)
  date = models.DateField(max_length=55)
  closure_date = models.DateField(auto_now=True)
  payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
