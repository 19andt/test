from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from .models import comment
from .serializers import CommentSerializer


class interest_list(ListCreateAPIView):
    # Querying all the records in the user table of the database
    queryset = comment.objects.all()
    # Initializing the user serializer class
    serializer_class = CommentSerializer


class interest_detail(RetrieveUpdateDestroyAPIView):
    # Querying all the records in the user table of the database
    queryset = comment.objects.all()
    # Initializing the user serializer class
    serializer_class = CommentSerializer