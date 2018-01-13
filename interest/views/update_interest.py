import json
from django.http import JsonResponse
from django.views import View
from interest.controller import InterestController


class UpdateInterestView(View):
    def post(self, request, *args, **kwargs):
        # Getting the data from the request
        data = json.loads(request.body.decode('utf-8'))
        # Checking if the user is authenticated
        if request.user.is_authenticated():
            # Updating the interests for the user
            InterestController.UpdateInterests(request.user, data['interests'])
            # Returning the response with update status
            return JsonResponse({'UpdateInterestStatus': True})
        else:
            # Returning the response with update status
            return JsonResponse({'UpdateInterestStatus': False})