from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from .models import rating_detail
from .serializers import RatingDetailSerializer


class rating_detail_list(ListCreateAPIView):
    # Querying all the records in the user table of the database
    queryset = rating_detail.objects.all()
    # Initializing the user serializer class
    serializer_class = RatingDetailSerializer


class rating_detail_detail(RetrieveUpdateDestroyAPIView):
    # Querying all the records in the user table of the database
    queryset = rating_detail.objects.all()
    # Initializing the user serializer class
    serializer_class = RatingDetailSerializer