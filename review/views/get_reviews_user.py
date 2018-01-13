import json
from django.http import JsonResponse
from django.views import View
from review.controller import ReviewController


class GetReviewsUserView(View):
    def get(self, request, *args, **kwargs):
        # Checking if the user is authenticated
        if request.user.is_authenticated():
            # Returning the response with reviews for the current logged in user
            return JsonResponse({'ReviewsList': ReviewController.GetReviewsForUser(User=request.user), 'MaxRating': 5})
        else:
            # Returning the response with no reviews
            return JsonResponse({'ReviewsList': {}, 'MaxRating': 5})