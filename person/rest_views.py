from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from .models import person
from .serializers import PersonSerializer


class person_list(ListCreateAPIView):
    # Querying all the records in the user table of the database
    queryset = person.objects.all()
    # Initializing the user serializer class
    serializer_class = PersonSerializer


class person_detail(RetrieveUpdateDestroyAPIView):
    # Querying all the records in the user table of the database
    queryset = person.objects.all()
    # Initializing the user serializer class
    serializer_class = PersonSerializer