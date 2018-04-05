from rest_framework import serializers
from .models import comment
from user.serializers import UserSerializer
from review.serializers import ReviewSerializer


class CommentSerializer(serializers.ModelSerializer):
    # Defining the serializer for the foreign key
    user=UserSerializer()
    # Defining the serializer for the foreign key
    review=ReviewSerializer()

    class Meta:
        # Defining the model for the serializer class
        model=comment
        # Defining the fields for the serializer class
        fields=('id', 'user', 'review', 'caption', 'description', 'created')