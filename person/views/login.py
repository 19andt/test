import json
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.views import View
from django.http import JsonResponse
from user.serializers import UserSerializer


class LoginView(View):
    def post(self, request, *args, **kwargs):
        # Getting the data from the request
        data=json.loads(request.body.decode('utf-8'))
        try:
            # Querying the user for the email.
            qs=User.objects.filter(email=data.get('email'))
            # Checking if the query objects returned is with only one user object
            if qs.count()==1 and qs[0]:
                user=qs[0]
                # Checking for the user password
                if not user.check_password(data.get('password')):
                    # Returning a response with the password as wrong
                    return JsonResponse({'LoginUserStatus': False, 'EmailPresent': True, 'PasswordWrong': True})
                else:
                    # Logging in the user and returning the user details
                    login(request, user)
                    return JsonResponse({'LoginUserStatus': True, 'User': UserSerializer(request.user).data})
            else:
                # Returning the response with multiple users present with the same email
                return JsonResponse({'LoginUserStatus': False, 'EmailPresent': True})
        except Exception as ex:
            print(ex)
            # Retuning response with could not login
            return JsonResponse({'LoginUserStatus': False, 'EmailPresent': False})