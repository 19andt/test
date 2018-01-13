from rest_framework import serializers
from .models import rating_detail
from user.serializers import UserSerializer


class RatingDetailSerializer(serializers.ModelSerializer):
    # Defining the serializer for the foreign key
    user=UserSerializer()

    class Meta:
        # Defining the serializer for the foreign key
        model=rating_detail
        # Defining the fields for the serializer class
        fields=('id', 'user', 'topic', 'one', 'two', 'three', 'four', 'five')