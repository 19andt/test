from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from .models import interest
from .serializers import InterestSerializer


class interest_list(ListCreateAPIView):
    # Querying all the records in the user table of the database
    queryset = interest.objects.all()
    # Initializing the user serializer class
    serializer_class = InterestSerializer


class interest_detail(RetrieveUpdateDestroyAPIView):
    # Querying all the records in the user table of the database
    queryset = interest.objects.all()
    # Initializing the user serializer class
    serializer_class = InterestSerializer