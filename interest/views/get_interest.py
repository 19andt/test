import json
from django.http import JsonResponse
from django.views import View
from interest.controller import InterestController
from topic.controller import TopicController


class GetInterestView(View):
    def get(self, request, *args, **kwargs):
        # Checking if the user is authenticated
        if request.user.is_authenticated():
            # Getting the interests for the user
            interest=InterestController.GetInterests(User=request.user)
            # Checking if the interests count is greater than zero
            if interest.count()>0:
                # Getting the topics from the interests
                topics=interest.values_list('topic', flat=True)
                interest=[]
                # Looping through the topics received
                for topic_id in topics:
                    # Getting the topic from ID
                    topic=TopicController.GetTopic(ID=topic_id)
                    # Checking if the topic is empty
                    if topic is not None:
                        # Appending the topic name to the interest
                        interest.append(topic[0].name)
            else:
                # Emptying the interest list
                interest=[]
                # Returning the response with the interest list
            return JsonResponse({'InterestList': interest, 'UserAuthenticated': True})
        else:
            # Returning the response without interest list
            return JsonResponse({'UserAuthenticated': False})