import json
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.views import View
from django.http import JsonResponse


class LogoutView(View):
    def post(self, request, *args, **kwargs):
        # Getting the data from the request
        data = json.loads(request.body.decode('utf-8'))
        # Checking if the user is authenticated
        if request.user.is_authenticated():
            # Logging out the user and returning the logging out response
            logout(request)
            return JsonResponse({'LogoutUserStatus':True})
        else:
            # Returning the user mismatch response
            return JsonResponse({'LogoutUserStatus':False})