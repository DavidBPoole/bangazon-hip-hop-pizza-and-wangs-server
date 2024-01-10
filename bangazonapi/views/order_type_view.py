"""View module for handling requests for orders type"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from bangazonapi.models import OrderType
from bangazonapi.serializers import OrderTypeSerializer

class OrderTypeView(ViewSet):
  """HHP&W order type view"""
  
  def retrieve(self, request, pk):
    """Handle GET reqeust for a single order type
    
    Returns -> Response -- JSON serialized order type"""
    
    try:
      ordertype = OrderType.objects.get(pk=pk)
      serializer = OrderTypeSerializer(ordertype)
      return Response(serializer.data)
    except OrderType.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request):
    """Handle GET requests for all order types
    
    Returns -> Response -- JSON serialized list of order types"""
    
    try:
      ordertypes = OrderType.objects.all()
      serializer = OrderTypeSerializer(ordertypes, many=True)
      return Response(serializer.data)
    except OrderType.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
