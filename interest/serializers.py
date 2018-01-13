from rest_framework import serializers
from .models import interest
from user.serializers import UserSerializer
from topic.serializers import TopicSerializer


class InterestSerializer(serializers.ModelSerializer):
    # Defining the serializer for the foreign key
    user=UserSerializer()
    # Defining the serializer for the foreign key
    topic=TopicSerializer()

    class Meta:
        # Defining the model for the serializer class
        model=interest
        # Defining the fields for the serializer class
        fields=('id', 'user', 'topic', 'timestamp')