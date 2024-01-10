from rest_framework import serializers
from bangazonapi.models import Order
from .item_serializer import ItemSerializer

class OrderSerializer(serializers.ModelSerializer):
  """JSON serializer for orders"""
  items = ItemSerializer(many=True)
  
  class Meta:
    model = Order
    fields = ('id', 'user', 'order_name', 'customer_phone', 'customer_email', 'order_type', 'order_total', 'timestamp', 'date', 'payment_type', 'order_status', 'is_closed')
    depth = 1
