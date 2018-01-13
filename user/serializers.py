from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # Defining the model for the serializer class
        model=User
        # Defining the fields for the serializer class
        fields=('id', 'first_name', 'username', 'email', 'date_joined', 'last_login')