import json, uuid
from django.http import JsonResponse
from django.views import View
from subscription.controller import SubscriptionController
from user.get_user import GetUser


class GetSubscriptionListView(View):
    def get(self, request, *args, **kwargs):
        # Getting the data from the request
        if request.user.is_authenticated():
            subscription=SubscriptionController.GetSubscriptions(User=request.user)

            if subscription.count() > 0:
                # Getting the topics from the interests
                reviewers = subscription.values_list('reviewer', flat=True)
                subscription = []
                # Looping through the topics received
                for reveiwer_id in reviewers:
                    # Getting the topic from ID
                    user = GetUser.get_user_by_id(ID=reveiwer_id)
                    # Checking if the topic is empty
                    if user is not None:
                        # Appending the topic name to the interest
                        subscription.append({
                            'name': user.first_name,
                            'username': user.username
                        })
            else:
                subscription = []
            return JsonResponse({'SubscriptionList': subscription, 'UserAuthenticated': True})
        return JsonResponse({'UserAuthenticated': False})