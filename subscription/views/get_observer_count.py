import json, uuid
from django.http import JsonResponse
from django.views import View
from subscription.controller import SubscriptionController


class GetObserverCountView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            count = SubscriptionController.GetObserverCount(User=request.user)
            print(count)
            return JsonResponse({'ObserverCount': count, 'UserAuthenticated': True})
        else:
            return JsonResponse({'UserAuthenticated': False})