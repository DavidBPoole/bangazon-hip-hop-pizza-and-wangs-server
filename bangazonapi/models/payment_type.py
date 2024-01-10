from django.db import models

class PaymentType(models.Model):

    type = models.CharField(max_length=55)
    