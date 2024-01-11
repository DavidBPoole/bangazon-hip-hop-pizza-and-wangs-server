from rest_framework import serializers
from bangazonapi.models import User

class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for the User model"""

    class Meta:
        model = User
        fields = ('id', 'username', 'uid')
