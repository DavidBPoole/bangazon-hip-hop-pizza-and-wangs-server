from django.db import models
from .item import Item
from .order import Order

class OrderItem(models.Model):
  order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
  item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
