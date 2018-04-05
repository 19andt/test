from rest_framework import serializers
from .models import review
from user.serializers import UserSerializer


class ReviewSerializer(serializers.ModelSerializer):
    # Defining the serializer for the foreign key
    added_by=UserSerializer()

    class Meta:
        # Defining the serializer for the foreign key
        model=review
        # Defining the fields for the serializer class
        fields=('id', 'added_by', 'caption', 'briefing', 'review_rating', 'created', 'updated')