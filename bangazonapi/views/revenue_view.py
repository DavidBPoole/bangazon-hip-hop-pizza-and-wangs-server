from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from bangazonapi.models import Revenue
from bangazonapi.serializers import RevenueSerializer

class RevenueView(ViewSet):
    """View for handling requests for revenue"""

    def retrieve(self, request, pk):
        """Handle GET request for a single revenue entry
        
        Returns -> Response -- JSON serialized revenue entry"""
        try:
            revenue = Revenue.objects.get(pk=pk)
            serializer = RevenueSerializer(revenue)
            return Response(serializer.data)
        except Revenue.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests for all revenue entries
        
        Returns -> Response -- JSON serialized list of revenue entries"""
        try:
            revenues = Revenue.objects.all()
            serializer = RevenueSerializer(revenues, many=True)
            return Response(serializer.data)
        except Revenue.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
