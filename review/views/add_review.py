import json
from django.http import JsonResponse
from django.views import View
from review.controller import ReviewController
from topic.controller import TopicController


class AddReviewView(View):
    def post(self, request, *args, **kwargs):
        # Getting a data from the request
        data = json.loads(request.body.decode('utf-8'))
        # Checking if the user is authenticated
        if request.user.is_authenticated():
            # Making a dictionary for the review parameters
            new_review={
                'added_by': request.user,
                'topic_list': data.get('topic_list'),
                'caption': data.get('caption'),
                'briefing': data.get('briefing'),
                'rating': data.get('rating')
            }
            # Adding the new review into the database
            if ReviewController.AddReview(new_review):
                # Returning the response with new review added
                return JsonResponse({'AddReviewStatus': True})
            else:
                # Returning the response with unable add new review
                return JsonResponse({'AddReviewStatus': False})