from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from .models import review_topic
from .serializers import RatingTopicSerializer


class review_topic_list(ListCreateAPIView):
    # Querying all the records in the user table of the database
    queryset = review_topic.objects.all()
    # Initializing the user serializer class
    serializer_class = RatingTopicSerializer


class review_topic_detail(RetrieveUpdateDestroyAPIView):
    # Querying all the records in the user table of the database
    queryset = review_topic.objects.all()
    # Initializing the user serializer class
    serializer_class = RatingTopicSerializer