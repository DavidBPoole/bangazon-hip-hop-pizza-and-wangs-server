from rest_framework import serializers
from .order_serializer import OrderSerializer
from .payment_type_serializer import PaymentTypeSerializer
from bangazonapi.models import Revenue

class RevenueSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    payment_type = PaymentTypeSerializer()

    class Meta:
        model = Revenue
        fields = [
            'id',
            'order',
            'total_revenue',
            'total_tips',
            'date_range',
            'date',
            'total_call_in',
            'total_walk_in',
            'closure_date',
            'payment_type',
        ]
