import json
from django.http import JsonResponse
from django.views import View
from interest.controller import InterestController
from topic.controller import TopicController


class EditInterestView(View):
    def get(self, request, topic_name, *args, **kwargs):
        if request.user.is_authenticated():
            qs = InterestController.GetInterest(User=request.user, Topic=TopicController.GetTopic(Name=topic_name))
            print(qs)
            if qs.count() == 1:
                return JsonResponse({'InterestStatus': True, 'UserAuthenticated': True})
            else:
                return JsonResponse({'InterestStatus': False, 'UserAuthenticated': True})
        else:
            return JsonResponse({'UserAuthenticated': False})

    def post(self, request, topic_name, *args, **kwargs):
        # Getting the data from the request
        data = json.loads(request.body.decode('utf-8'))
        print(data)
        if request.user.is_authenticated():
            if data.get('update_interest_status'):
                if InterestController.AddInterests(User=request.user, Data=[{
                    'type': 'old',
                    'text': topic_name
                }]):
                    return JsonResponse({'InterestStatus': True, 'UpdateInterestStatus': True, 'UserAuthenticated': True})
                else:
                    qs = InterestController.GetInterest(User=request.user,
                                                        Topic=TopicController.GetTopic(Name=topic_name))
                    print(qs)
                    if qs.count() == 1:
                        return JsonResponse({'InterestStatus': True,'UpdateInterestStatus': False, 'UserAuthenticated': True})
                    else:
                        return JsonResponse({'InterestStatus': False, 'UpdateInterestStatus': False, 'UserAuthenticated': True})
            else:
                InterestController.DeleteInterest(User=request.user, Topic=TopicController.GetTopic(Name=topic_name))
                return JsonResponse({'InterestStatus': False, 'UpdateInterestStatus': True, 'UserAuthenticated': True})
        else:
            return JsonResponse({'UserAuthenticated': False})