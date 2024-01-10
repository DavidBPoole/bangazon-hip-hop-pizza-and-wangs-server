from rest_framework import serializers
from bangazonapi.models import Item

class ItemSerializer(serializers.ModelSerializer):
  """JSON serializer for the menu"""
  
  class Meta:
    model = Item
    fields = ('id', 'item_name', 'item_price')
    depth = 1
    