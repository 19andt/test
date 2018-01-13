import json
from django.http import JsonResponse
from django.views import View
from rating.controller import RatingController
from review.controller import ReviewController


class UpdateRatingView(View):
    def post(self, request, *args, **kwargs):
        # Getting the data from the request
        data = json.loads(request.body.decode('utf-8'))
        # Checking if the user is authenticated
        if request.user.is_authenticated():
            # Getting the review by the ID
            review=ReviewController.GetReviewByID(data.get('review_id'))
            # Checking if the review is empty
            if review!=None:
                # Update the user rating for the review
                if RatingController.UpdateRating(request.user, review, data.get('value')):
                    # Returning the response with update status
                    return JsonResponse({'UpdateRatingStatus': True})
                else:
                    # Returning the response with update status
                    return JsonResponse({'UpdateRatingStatus': False})
            else:
                return JsonResponse({'UpdateRatingStatus':False})