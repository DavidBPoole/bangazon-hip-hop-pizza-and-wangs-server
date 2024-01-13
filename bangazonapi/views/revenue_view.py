from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bangazonapi.models import Revenue


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
        """Handle GET requests to get all revenue nodes.
        Returns: Response -- JSON serialized list of revenue nodes"""

        try:
            revenues = Revenue.objects.all()
            serializer = RevenueSerializer(revenues, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'message': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RevenueSerializer(serializers.ModelSerializer):
    """JSON serializer for revenue nodes"""
    class Meta:
        model = Revenue
        fields = ('id', 'order', 'date', 'payment', 'subtotal', 'tip', 'total')
        depth = 1
