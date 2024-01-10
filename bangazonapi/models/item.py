from django.db import models

class Item(models.Model):
  item_name = models.CharField(max_length=55)
  item_price = models.DecimalField(max_digits=7, decimal_places=2)
