import json, uuid
from django.http import JsonResponse
from django.views import View
from user.get_user import GetUser
from user.serializers import UserSerializer


class GetLoggedInUserView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return JsonResponse({'User': UserSerializer(request.user).data, 'UserAuthenticated': True})
        else:
            return JsonResponse({'UserAuthenticated': False})