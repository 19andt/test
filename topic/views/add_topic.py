import json, random,string
from django.http import JsonResponse
from django.views import View
from topic.controller import TopicController
from interest.controller import InterestController


class AddTopicView(View):
    def post(self, request, *args, **kwargs):
        # Getting the data from the request
        data=json.loads(request.body.decode('utf-8'))
        # Checking if the user is authenticated
        if request.user.is_authenticated():
            # Making a dictionary for the review parameters
            new_topic={
                'name': data.get('name'),
                'description': data.get('description'),
                'added_by': request.user,
            }
            # Adding the new review into the database
            if TopicController.AddTopic(new_topic):
                InterestController.AddInterests(User=request.user, Data=[{
                    'type': 'old',
                    'text': data.get('name')
                }])
                # Returning the response with new review added
                return JsonResponse({'AddTopicStatus': True})
            else:
                # Returning the response with unable add new review
                return JsonResponse({'AddTopicStatus': False})