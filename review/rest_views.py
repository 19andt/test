from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from .models import review
from .serializers import ReviewSerializer


class review_list(ListCreateAPIView):
    # Querying all the records in the user table of the database
    queryset = review.objects.all()
    # Initializing the user serializer class
    serializer_class = ReviewSerializer


class review_detail(RetrieveUpdateDestroyAPIView):
    # Querying all the records in the user table of the database
    queryset = review.objects.all()
    # Initializing the user serializer class
    serializer_class = ReviewSerializer