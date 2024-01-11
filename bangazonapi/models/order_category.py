from django.db import models

class OrderCategory(models.Model):
    category = models.CharField(max_length=55)
