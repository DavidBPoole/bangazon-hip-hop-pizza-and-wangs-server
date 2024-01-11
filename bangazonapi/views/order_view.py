"""View module for handling requests for orders"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from bangazonapi.models import Order, User, OrderType, PaymentType, OrderItem, Item
from bangazonapi.serializers import OrderSerializer

class OrderView(ViewSet):
  """Hip Hop, Pizza, & Wings Order View"""
  
  def retrieve(self, request, pk):
    """Handle GET request for a single order
    
    Returns -> Response -- JSON serialized order"""
    
    try:
      order = Order.objects.get(pk=pk)
      
      #---Putting items on orders logic----
      item_list = OrderItem.objects.filter(order_id = order.pk)
      items = []
      
      for e in item_list:
        items.append(e.item_id)
        
      order.items = Item.objects.filter(pk__in = items)
      #-----------------------------------
      serializer = OrderSerializer(order)
      return Response(serializer.data)
    except Order.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request):
    """Handle GET requests for all orders
    
    Returns -> Response -- JSON serialized list of orders"""
    
    try:
      orders = Order.objects.all()
      
      #----Putting items on orders logic---
      for order in orders:
        item_list = OrderItem.objects.filter(order_id = order.pk)
        items = []
        for e in item_list:
          items.append(e.item_id)

        order.items = Item.objects.filter(pk__in = items)
      #------------------------------------
      serializer = OrderSerializer(orders, many=True)
      return Response(serializer.data)
    except Order.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def create(self, request):
    """Handle POST request for orders
    Returns -> JSON serialized order instance with 201 status"""
    user = User.objects.get(pk=request.data['username'])
    type = OrderType.objects.get(pk=request.data['type'])
    payment = PaymentType.objects.get(pk=request.data['payment'])
    
    order = Order.objects.create(
      user = user,
      is_closed = request.data['isClosed'],
      order_name = request.data['orderName'],
      customer_phone = request.data['customerPhone'],
      customer_email = request.data['customerEmail'],
      order_type = request.data['orderType'],
      order_total = request.data['orderTotal'],
      timestamp = request.data['timestamp'],
      date = request.data['date'],
      payment_type = request.data['paymentType'],
      type = type,
      payment = payment,
    )
    
    serializer = OrderSerializer(order)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def update(self, request, pk):
    """Handles PUT requests for an order
    
    Returns -> JSON serialized order instance with 200 status"""
    
    user = User.objects.get(pk=request.data['username'])
    type = OrderType.objects.get(pk=request.data['type'])
    payment = PaymentType.objects.get(pk=request.data['payment'])
    
    order = Order.objects.get(pk=pk)
    
    order.user = user
    order.is_closed = request.data['isClosed']
    order.order_name = request.data['orderName']
    order.customer_phone = request.data['customerPhone']
    order.customer_email = request.data['customerEmail']
    order.order_type = request.data['orderType']
    order.order_total = request.data['orderTotal']
    order.timestamp = request.data['timestamp']
    order.date =request.data['date']
    order.payment_type = request.data['paymentType']
    order.status = request.data['orderStatus']
    order.type = type
    order.payment = payment
    
    order.save()
    serializer = OrderSerializer(order)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def destroy(self, reqeust, pk):
    """Handles Delete request for an order
    
    Returns -> Empty body with 204 status"""
    
    order = Order.objects.get(pk=pk)
    order.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    