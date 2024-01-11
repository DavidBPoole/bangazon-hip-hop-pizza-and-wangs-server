"""View module for handling requests for payment types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from bangazonapi.models import PaymentType
from bangazonapi.serializers import PaymentTypeSerializer

class PaymentTypeView(ViewSet):
  """Payment type view"""
  
  def retrieve(self, request, pk):
    """Handle GET request for single payment type
    
    Returns -> Response -- JSON serialized payment type"""
    
    try:
      paymenttype = PaymentType.objects.get(pk=pk)
      serializer = PaymentTypeSerializer(paymenttype)
      return Response(serializer.data)
    except PaymentType.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request):
    """Handle GET request for all payment types
    
    Returns -> Response -- JSON serialized list of payment types"""
    
    try:
      paymenttypes = PaymentType.objects.all()
      serializer = PaymentTypeSerializer(paymenttypes, many=True)
      return Response(serializer.data)
    except PaymentType.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    