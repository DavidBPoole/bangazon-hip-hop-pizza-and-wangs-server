"""View module for handling requests for orders items"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from bangazonapi.models import Order, OrderItem, Item
from bangazonapi.serializers import OrderItemSerlializer

class OrderItemView(ViewSet):
  """HHP&W Order Item Join Table View"""
  
  def retrieve(self, request, pk):
    """Hande GET requests for a single order item
    
    Returns -> Response -- JSON serialized Order Item"""
    
    try:
      orderitem = OrderItem.objects.get(pk=pk)
      serializer = OrderItemSerlializer(orderitem)
      return Response(serializer.data)
    except OrderItem.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request):
    """Handle GET request for all order items
    
    Returns -> Response -- JSON serialized list of order items"""
    
    try:
      orderitems = OrderItem.objects.all()
      serializer = OrderItemSerlializer(orderitems, many=True)
      return Response(serializer.data)
    except OrderItem.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def create(self, request):
    """Handle POST requests for order items
    
    Returns -> JSON serialized order item instance with 201 status"""
    
    order = Order.objects.get(pk=request.data['order'])
    item = Item.objects.get(pk=request.data['item'])
    
    orderitem = OrderItem.objects.create(
      order = order,
      item = item,
      quantity = request.data['quantity']
    )
    
    serializer = OrderItemSerlializer(orderitem)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def update(self, request, pk):
    """Handles PUT requests for an order item
    
    Returns -> JSON serialized order itme instance with 200 status"""
    
    orderitem = OrderItem.objects.get(pk=pk)
    order = Order.objects.get(pk=request.data['order'])
    item = Item.objects.get(pk=request.data['item'])
    
    orderitem.order = order
    orderitem.item = item
    
    orderitem.save()
    serializer = OrderItemSerlializer(orderitem)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def destroy(self, request, pk):
    """Handles Delete request for an order item
    
    Returns -> Empty body with 204 status"""
    
    orderitem = OrderItem.objects.get(pk=pk)
    orderitem.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
    