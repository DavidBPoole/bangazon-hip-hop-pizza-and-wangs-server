from rest_framework import serializers
from bangazonapi.models import OrderType

class OrderTypeSerializer(serializers.ModelSerializer):
  """JSON serializer for an orders type"""
  
  class Meta:
    model = OrderType
    fields = ('id', 'label')
