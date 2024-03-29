from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bangazonapi.models import OrderItem, Order, Item


class OrderItemView(ViewSet):
    """order item view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single order item.
        Returns: Response -- JSON serialized order item"""

        try:
            order_item = OrderItem.objects.get(pk=pk)
            serializer = OrderItemSerializer(order_item)
            return Response(serializer.data)
        except OrderItem.DoesNotExist:
            return Response({'message': 'OrderItem not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def list(self, request):
        """Handle GET requests to get all order_items.
        Returns: Response -- JSON serialized list of order_items"""
        order_items = OrderItem.objects.all()
        serializer = OrderItemSerializer(order_items, many=True)
        return Response(serializer.data)


class OrderItemSerializer(serializers.ModelSerializer):
    """JSON serializer for order items"""
    name = serializers.CharField(source='item.name', read_only=True)
    price = serializers.DecimalField(source='item.price', read_only=True, max_digits=7, decimal_places=2)

    class Meta:
        model = OrderItem
        fields = ('id', 'name', 'price')
        depth = 1
