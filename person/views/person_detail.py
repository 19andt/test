import json
from django.http import JsonResponse
from django.views import View
from person.models import person
from person.serializers import PersonSerializer
from user.get_user import GetUser


class PersonDetailView(View):
    def get(self, request, username, *args, **kwargs):
        # Checking if the username is empty
        if not username=='':
            # Getting the user with the current username
            user=GetUser.get_user_by_username(username=username)
            # Checking the user exits with the current username
            if user==None:
                # Returning the response with no username
                return JsonResponse({'PersonStatus': False})
            # Querying for the personal details of the user
            qs=person.objects.filter(user=user)
            # Checking if query results is equal to one
            if qs.count()==1:
                # Retuning the response with the query results
                return JsonResponse({'Person': PersonSerializer(qs[0]).data, 'PersonStatus': True})
            else:
                # Returning the response with no user
                return JsonResponse({'PersonStatus': False})
        else:
            # Retuning the response with no user
            return JsonResponse({'PersonStatus': False})


    def post(self, request, username, *args, **kwargs):
        # Getting the data from the request
        data=json.loads(request.body.decode('utf-8'))
        # Checking if the username is empty
        if not username=='':
            # Querying for the user
            user=GetUser.get_user_by_username(username=username)
            # Checking if the query results is empty
            if user==None:
                # Returning the user status
                return JsonResponse({'PersonStatus': False})
            # Querying for the person
            qs=person.objects.filter(user=user)
            # Checking if the query results is equal to one
            if qs.count()==1:
                # Updating the user data with the data from the request
                user.first_name=data.person.user.full_name
                user.email=data.person.user.email
                # Saving the user details
                user.save()
                person.mobile_number=data.person.mobile_number
                person.pic=data.person.pic
                # Saving the person details
                person.save()
                # Returning the response with update status of the user
                return JsonResponse({'PersonStatus': True})
            else:
                # Returning the response with unable update status of the user
                return JsonResponse({'PersonStatus': False})
        else:
            # Returning the response with no user
            return JsonResponse({'PersonStatus': False})