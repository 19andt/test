import json, uuid
from django.http import JsonResponse
from django.views import View
from subscription.controller import SubscriptionController
from user.get_user import GetUser


class SubscriptionStatusView(View):
    def get(self, request, username, *args, **kwargs):
        # Getting the data from the request
        if request.user.is_authenticated():
            if request.user.username == username:
                return JsonResponse({'PrimaryUser': True, 'SubscriptionStatus': False, 'UserAuthenticated': True})
            qs=SubscriptionController.GetSubscription(
                Observer=request.user,
                Reviewer=GetUser.get_user_by_username(username=username))
            if qs.count() == 1:
                return JsonResponse({'SubscriptionStatus': True, 'UserAuthenticated': True})
            else:
                return JsonResponse({'SubscriptionStatus': False, 'UserAuthenticated': True})
        return JsonResponse({'UserAuthenticated': False})

    def post(self, request, username, *args, **kwargs):
        # Getting the data from the request
        data = json.loads(request.body.decode('utf-8'))
        print(data)
        if request.user.is_authenticated():
            if data.get('update_subscription_status'):
                if SubscriptionController.AddSubscription(
                        Observer=request.user,
                        Reviewer=GetUser.get_user_by_username(username=username)):
                    return JsonResponse(
                        {
                            'SubscriptionStatus': True,
                            'UpdateSubscriptionStatus': True,
                            'UserAuthenticated': True
                        })
                else:
                    qs = SubscriptionController.GetSubscription(
                        Observer=request.user,
                        Reviewer=GetUser.get_user_by_username(username=username))
                    if qs.count() == 1:
                        return JsonResponse(
                            {
                                'SubscriptionStatus': True,
                                'UpdateSubscriptionStatus': False,
                                'UserAuthenticated': True
                            })
                    else:
                        return JsonResponse(
                            {
                                'SubscriptionStatus': False,
                                'UpdateSubscriptionStatus': False,
                                'UserAuthenticated': True
                            })
            else:
                SubscriptionController.DeleteSubscription(
                    Observer=request.user,
                    Reviewer=GetUser.get_user_by_username(username=username))
        return JsonResponse(
            {
                'SubscriptionStatus': False,
                'UpdateSubscriptionStatus': True,
                'UserAuthenticated': True
            })