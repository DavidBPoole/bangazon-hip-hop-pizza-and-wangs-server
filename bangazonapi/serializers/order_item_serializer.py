from rest_framework import serializers
from bangazonapi.models import OrderItem

class OrderItemSerlializer(serializers.ModelSerializer):
  """JSON serializer for an orders items"""
  
  class Meta:
    model = OrderItem
    fields = ('id', 'order_id', 'item_id')
