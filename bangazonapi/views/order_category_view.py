"""View module for handling order category requests"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bangazonapi.models import OrderCategory
from bangazonapi.serializers import OrderCategorySerializer

class OrderCategoryView(ViewSet):
  """Payment Type View"""
  
  def retrieve(self, request, pk):
    """Handles GET request for single order category option"""
    
    try:
      order_category = OrderCategory.objects.get(pk=pk)
      serializer = OrderCategorySerializer(order_category)
      return Response(serializer.data)
    except OrderCategory.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

  def list(self, request):
    """Handles GET request for all order category options"""
    
    order_category = OrderCategory.objects.all()
    serializer = OrderCategorySerializer(order_category, many=True)
    return Response(serializer.data)
