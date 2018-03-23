import json
from django.http import JsonResponse
from django.views import View
from review.controller import ReviewController
from user.get_user import GetUser


class GetReviewsByUserView(View):
    def get(self, request, username, *args, **kwargs):
        # Checking if the user is authenticated
        if request.user.is_authenticated():
            # Returning the response with reviews for the current logged in user
            return JsonResponse({'ReviewsList': ReviewController.GetReviewsByUser(User=GetUser.get_user_by_username(username=username)), 'MaxRating': 5, 'PrimaryUser': True})
        else:
            # Returning the response with no reviews
            return JsonResponse({'ReviewsList': ReviewController.GetReviewsByUser(User=GetUser.get_user_by_username(username=username)), 'MaxRating': 5, 'PrimaryUser': False})