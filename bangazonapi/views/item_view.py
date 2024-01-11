"""View module for handling request for menu"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from bangazonapi.models.item import Item
from bangazonapi.serializers import ItemSerializer

class ItemView(ViewSet):
  """Hip Hop, Pizza, & Wings Menu View"""
  
  def retrieve(self, request, pk):
    """Handle GET request for a single menu item
    
    Returns -> Response -- JSON serlialized menu"""
    
    try:
      menu = Item.objects.get(pk=pk)
      serializer = ItemSerializer(menu)
      return Response(serializer.data)
    except Item.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request):
    """Handles GET request for all menu items
    
    Returns -> Response -- JSON serialized list of artists"""
    
    try:
      menus = Item.objects.all()
      serializer = ItemSerializer(menus, many=True)
      return Response(serializer.data)
    except Item.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
