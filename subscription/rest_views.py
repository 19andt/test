from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from .models import subscription
from .serializers import SubscriptionSerializer


class subscription_list(ListCreateAPIView):
    # Querying all the records in the user table of the database
    queryset = subscription.objects.all()
    # Initializing the user serializer class
    serializer_class = SubscriptionSerializer


class subscription_detail(RetrieveUpdateDestroyAPIView):
    # Querying all the records in the user table of the database
    queryset = subscription.objects.all()
    # Initializing the user serializer class
    serializer_class = SubscriptionSerializer