from django.http import JsonResponse
from django.views import View
from user.serializers import UserSerializer


class CheckAuthenticationView(View):
    def get(self, request, *args, **kwargs):
        # Checking if the user is authenticated
        if request.user.is_authenticated():
            # Checking if the user is a super user
            if request.user.is_superuser:
                # returning the response along with super user data
                return JsonResponse({'UserAuthenticated': True, 'SuperUser': True})
            else:
                # Returning the response along with the user details
                return JsonResponse({'UserAuthenticated': True, 'User': UserSerializer(request.user).data, 'SuperUser': False})
        else:
            # Returning the response
            return JsonResponse({'UserAuthenticated': False})