from rest_framework import serializers
from .models import topic
from user.serializers import UserSerializer


class TopicSerializer(serializers.ModelSerializer):
    # Defining the serializer for the foreign key
    added_by=UserSerializer()

    class Meta:
        # Defining the model for the serializer class
        model=topic
        # Defining the fields for the serializer class
        fields=('id', 'name', 'added_by', 'timestamp', 'description')