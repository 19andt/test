from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from .models import rating
from .serializers import RatingSerializer


class rating_list(ListCreateAPIView):
    # Querying all the records in the user table of the database
    queryset = rating.objects.all()
    # Initializing the user serializer class
    serializer_class = RatingSerializer


class rating_detail(RetrieveUpdateDestroyAPIView):
    # Querying all the records in the user table of the database
    queryset = rating.objects.all()
    # Initializing the user serializer class
    serializer_class = RatingSerializer