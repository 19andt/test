import json
from django.http import JsonResponse
from django.views import View
from review.controller import ReviewController
from review.serializers import ReviewSerializer
from rating.controller import RatingController


class GetReviewView(View):
    def get(self, request, id, *args, **kwargs):
        # Checking if the user is authenticated
        if request.user.is_authenticated():
            # Getting the review by ID
            review=ReviewController.GetReviewByID(ID=id)
            # Checking if the review is empty
            if review is not None:
                # Returning the response with the review details
                return JsonResponse({'Review': ReviewSerializer(review).data, 'Rating':RatingController.GetRating(Person=request.user, Review=review), 'MaxRating': 5})
            else:
                # Returning the response with unable to find the review
                return JsonResponse({'Review': None, 'MaxRating': 5})
        else:
            # Returning the response with unable to find the review
            return JsonResponse({'Review': None, 'MaxRating': 5})