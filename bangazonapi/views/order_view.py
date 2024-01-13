from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from bangazonapi.models import Order, User, Item, OrderItem
from bangazonapi.views.order_item_view import OrderItemSerializer


class OrderView(ViewSet):
    """order view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single order.
        Returns: Response -- JSON serialized order"""

        try:
            order = Order.objects.get(pk=pk)
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        except Order.DoesNotExist:
            return Response({'message': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests to get all orders.
        Returns: Response -- JSON serialized list of orders"""
        try:
            orders = Order.objects.all()
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'message': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request):
        """Handle POST operations
        Returns Response -- JSON serialized order instance"""
        try:
            user = User.objects.get(id=request.data["user"])

            order = Order.objects.create(
                user=user,
                name=request.data["name"],
                open=request.data["open"],
                phone=request.data["phone"],
                email=request.data["email"],
                type=request.data["type"],
            )
            serializer = OrderSerializer(order)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk):
        """Handle PUT requests for an order
        Returns: Response -- Empty body with 204 status code"""

        try:
            order = Order.objects.get(pk=pk)
            order.name = request.data["name"]
            order.phone = request.data["phone"]
            order.email = request.data["email"]
            order.type = request.data["type"]
            order.open = request.data["open"]

            order.save()

            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Order.DoesNotExist:
            return Response({'message': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk):
        """Handle DELETE requests for an order
        Returns: Response -- Empty body with 204 status code"""

        try:
            order = Order.objects.get(pk=pk)
            order.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Order.DoesNotExist:
            return Response({'message': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    # Add & Remove Order Items

    @action(methods=['post'], detail=True)
    def add_order_item(self, request, pk, item_id=None):
        """Post request for a user to add an item to an order"""
        try:
            # item = Item.objects.get(pk=request.data["item"])
            item = Item.objects.get(pk=item_id)
            order = Order.objects.get(pk=pk)

            if not order.open:
                return Response({'error': 'Cannot add item to a closed order.'}, status=status.HTTP_400_BAD_REQUEST)

            orderitem = OrderItem.objects.create(item=item, order=order)
            return Response({'message': 'Item added to order'}, status=status.HTTP_201_CREATED)
        except Item.DoesNotExist:
            return Response({'error': 'Item not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Order.DoesNotExist:
            return Response({'error': 'Order not found.'}, status=status.HTTP_404_NOT_FOUND)

    @action(methods=['delete'], detail=True)
    def remove_order_item(self, request, pk, order_item=None):
        """Delete request for a user to remove an item from an order"""
        try:
            # orderitem = OrderItem.objects.get(pk=request.data.get("order_item"), order__pk=pk)
            order_item_id = self.kwargs.get('order_item')
            orderitem = OrderItem.objects.get(pk=order_item_id, order__pk=pk)

            if not orderitem.order.open:
                return Response({'error': 'Cannot remove item from a closed order.'}, status=status.HTTP_400_BAD_REQUEST)

            orderitem.delete()
            return Response("Order item removed", status=status.HTTP_204_NO_CONTENT)
        except OrderItem.DoesNotExist:
            return Response({'error': 'Order item not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    # @action(methods=['delete'], detail=True)
    # def remove_order_item(self, request, pk):
    #     """Delete request for a user to remove an item from an order"""

    #     orderitem = request.data.get("order_item")
    #     OrderItem.objects.filter(pk=orderitem, order__pk=pk).delete()

    #     return Response("Order item removed", status=status.HTTP_204_NO_CONTENT)

class OrderSerializer(serializers.ModelSerializer):
    """JSON serializer for orders"""
    items = OrderItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Order
        fields = ('id', 'user', 'name', 'open', 'phone', 'email', 'type', 'items')
        depth = 1
