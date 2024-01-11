from rest_framework import serializers
from bangazonapi.models import OrderCategory

class OrderCategorySerializer(serializers.ModelSerializer):
  """JSON serializer for the menu"""
  
  class Meta:
    model = OrderCategory
    fields = ('id', 'category')
    depth = 1
