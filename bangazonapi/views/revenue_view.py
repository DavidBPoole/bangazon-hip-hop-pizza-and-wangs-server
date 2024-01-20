from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bangazonapi.models import Revenue, Order
# from django.db.models import Sum, Count

class RevenueView(ViewSet):
    """revenue view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single revenue.
        Returns: Response -- JSON serialized revenue"""

        try:
            revenue = Revenue.objects.get(pk=pk)
            serializer = RevenueSerializer(revenue)
            return Response(serializer.data)
        except Revenue.DoesNotExist:
            return Response({'message': 'Revenue not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        revenues = Revenue.objects.all()
        serializer = RevenueSerializer(revenues, many=True)
        return Response(serializer.data)
        
    def create(self, request):
        """Create Revenue Entry"""
        order_id = Order.objects.get(pk=request.data["orderId"])
        
        revenue = Revenue.objects.create(
            order=order_id,
            date=request.data["date"],
            payment=request.data["paymentType"],
            subtotal=request.data["subtotal"],
            total=request.data["total"],
            tip=request.data["tip"],
        )
        
        revenue.save()
        serializer = RevenueSerializer(revenue)
        return Response(serializer.data)


class RevenueSerializer(serializers.ModelSerializer):
    """JSON serializer for revenue nodes"""
    class Meta:
        model = Revenue
        fields = ("__all__")
        depth = 2
                                                                  

# Custom def create function to perform serveral functions at once like totaling the sum, changing order status, and adding the tip to total.

    # def create(self, request):
    #     """Handles POST operations

    #     Returns Response - JSON serialized Revenue instance"""
    #     total_amount = 0

    #     order = Order.objects.get(id=request.data["orderId"])
    #     order.open = False
    #     order.save()

    #     order_items = OrderItem.objects.filter(order=order)

    #     for order_item in order_items:
    #         total_amount += order_item.item.price
    #     total_amount += request.data["tip"]

    #     revenue = Revenue.objects.create(
    #         total=total_amount,
    #         payment=request.data["payment"],
    #         tip=request.data["tip"],
    #         order_type=order.type,
    #         order=order
    #     )
    #     serializer = RevenueSerializer(revenue)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    