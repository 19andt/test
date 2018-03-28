import json
from datetime import datetime
from django.http import JsonResponse
from django.views.generic import View
from subscription.controller import SubscriptionController
from subscription.serializers import SubscriptionSerializer
from review.controller import ReviewController
from review.serializers import ReviewSerializer


class NotificationView(View):
    def get(self, request, *args, **kwargs):
        # Checking if user is authenticated
        if request.user.is_authenticated():
            # Getting the new subscription count
            observers = []

            for item in SubscriptionController.GetObservers(request.user):
                if item.timestamp > request.user.last_login:
                    observers.append(SubscriptionSerializer(item).data)
            # Getting the new review count
            reviews = []

            for item in ReviewController.ReviewsForUser(request.user):
                if item.created > request.user.last_login and item.added_by != request.user:
                    reviews.append(ReviewSerializer(item).data)

            # Returning the response with reviews and subscription list
            return JsonResponse({'Reviews': reviews, 'Observers': observers, 'UserAuthenticated': True})
        else:
            # User is not authenticated
            return JsonResponse({'UserAuthenticated': False})

    def post(self, request, *args, **kwargs):
        # Checking if user is authenticated
        if request.user.is_authenticated():
            request.user.last_login = datetime.now()
            request.user.save()
        return JsonResponse({})