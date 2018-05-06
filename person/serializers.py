from rest_framework import serializers
from .models import person
from user.serializers import UserSerializer


class PersonSerializer(serializers.ModelSerializer):
    # Defining the serializer for the foreign key
    user=UserSerializer()

    class Meta:
        # Defining the model for the serializer class
        model=person
        # Defining the fields for the serializer class
        fields=('id', 'user', 'gender', 'mobile_number', 'bio', 'type', 'updated', 'pic', 'width_field', 'height_field', 'pic_url')