import json
from django.http import JsonResponse
from django.views import View
from review.controller import ReviewController
from topic.controller import TopicController
from user.serializers import UserSerializer


class GetReviewsTopicView(View):
    def get(self, request, topic_name, *args, **kwargs):
        # Checking if the user is authenticated
        if request.user.is_authenticated():
            # Getting the topic from the topic controller
            topic=TopicController.GetTopic(Name=topic_name)
            # Returning the response with reviews for the topic
            return JsonResponse({'ReviewsList': ReviewController.GetReviewsForTopic(Topic=topic, User=request.user), 'MaxRating': 5, 'User': UserSerializer(request.user).data})
        else:
            # Returning the response with no reviews
            return JsonResponse({'ReviewsList': {}, 'MaxRating': 5})