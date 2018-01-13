from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from .serializers import UserSerializer


class user_list(ListCreateAPIView):
    # Querying all the records in the user table of the database
    queryset = User.objects.all()
    # Initializing the user serializer class
    serializer_class = UserSerializer


class user_detail(RetrieveUpdateDestroyAPIView):
    # Querying all the records in the user table of the database
    queryset = User.objects.all()
    # Initializing the user serializer class
    serializer_class = UserSerializer
