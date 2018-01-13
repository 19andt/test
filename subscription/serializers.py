from rest_framework import serializers
from .models import subscription
from user.serializers import UserSerializer


class SubscriptionSerializer(serializers.ModelSerializer):
    # Defining the serializer for the foreign key
    observer=UserSerializer()
    # Defining the serializer for the foreign key
    reviewer=UserSerializer()

    class Meta:
        # Defining the model for the serializer class
        model=subscription
        # Defining the fields for the serializer class
        fields=('id', 'observer', 'reviewer', 'timestamp')