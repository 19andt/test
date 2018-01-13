from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from .models import topic
from .serializers import TopicSerializer


class topic_list(ListCreateAPIView):
    # Querying all the records in the user table of the database
    queryset = topic.objects.all()
    # Initializing the user serializer class
    serializer_class = TopicSerializer


class topic_detail(RetrieveUpdateDestroyAPIView):
    # Querying all the records in the user table of the database
    queryset = topic.objects.all()
    # Initializing the user serializer class
    serializer_class = TopicSerializer