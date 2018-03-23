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
            primary_user = None
            if request.user.username == username:
                primary_user = True
            else:
                primary_user = False
            # Querying for the personal details of the user
            qs=person.objects.filter(user=user)
            # Checking if query results is equal to one
            if qs.count()==1:
                # Retuning the response with the query results
                return JsonResponse({'Person': PersonSerializer(qs[0]).data, 'PrimaryUser': primary_user, 'PersonStatus': True})
            else:
                # Returning the response with no user
                return JsonResponse({'PrimaryUser': primary_user, 'PersonStatus': False})
        else:
            # Retuning the response with no user
            return JsonResponse({'PersonStatus': False})


    def post(self, request, username, *args, **kwargs):
        # Getting the data from the request
        data=json.loads(request.body.decode('utf-8'))
        # Checking if the username is empty
        if request.user.username == username:
            # Querying for the user
            user = GetUser.get_user_by_username(username=username)
            # Checking if the query results is empty
            if user == None:
                # Returning the user status
                return JsonResponse({'UpdateStatus': False})
            # Querying for the person
            qs=person.objects.filter(user=user)
            # Checking if the query results is equal to one
            if qs.count() == 1:
                # Updating the user data with the data from the request
                if data.get('full_name') != None:
                    user.first_name = data.get('full_name')
                if data.get('email') != None:
                    user.email = data.get('email')
                # Saving the user details
                user.save()

                current_person = user.person
                print(current_person)

                if data.get('mobile_number') != None:
                    current_person.mobile_number = data.get('mobile_number')
                if data.get('pic') != None:
                    current_person.pic = data.get('pic')
                if data.get('bio') != None:
                    current_person.bio = data.get('bio')
                # Saving the person details
                current_person.save()
                # Returning the response with update status of the user
                return JsonResponse({'UpdateStatus': True})
            else:
                # Returning the response with unable update status of the user
                return JsonResponse({'UpdateStatus': False})
        else:
            # Returning the response with no user
            return JsonResponse({'UpdateStatus': False})