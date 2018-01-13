from rest_framework import serializers
from .models import rating
from user.serializers import UserSerializer
from review.serializers import ReviewSerializer


class RatingSerializer(serializers.ModelSerializer):
    # Defining the serializer for the foreign key
    user=UserSerializer()
    # Defining the serializer for the foreign key
    review=ReviewSerializer()

    class Meta:
        # Defining the serializer for the foreign key
        model=rating
        # Defining the fields for the serializer class
        fields=('id', 'user', 'review', 'value')