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
                return JsonResponse({'FollowingStatus': True, 'UserAuthenticated': True})
            else:
                return JsonResponse({'FollowingStatus': False, 'UserAuthenticated': True})
        else:
            return JsonResponse({'UserAuthenticated': False})

    def post(self, request, topic_name, *args, **kwargs):
        # Getting the data from the request
        data = json.loads(request.body.decode('utf-8'))
        print(data)
        if request.user.is_authenticated():
            if data.get('update_following_status'):
                if InterestController.AddInterests(User=request.user, Data=[{
                    'type': 'old',
                    'text': topic_name
                }]):
                    return JsonResponse({'FollowingStatus': True, 'UpdateFollowingStatus': True, 'UserAuthenticated': True})
                else:
                    qs = InterestController.GetInterest(User=request.user,
                                                        Topic=TopicController.GetTopic(Name=topic_name))
                    print(qs)
                    if qs.count() == 1:
                        return JsonResponse({'FollowingStatus': True,'UpdateFollowingStatus': False, 'UserAuthenticated': True})
                    else:
                        return JsonResponse({'FollowingStatus': False, 'UpdateFollowingStatus': False, 'UserAuthenticated': True})
            else:
                InterestController.DeleteInterest(User=request.user, Topic=TopicController.GetTopic(Name=topic_name))
                return JsonResponse({'FollowingStatus': False, 'UpdateFollowingStatus': True, 'UserAuthenticated': True})
        else:
            return JsonResponse({'UserAuthenticated': False})