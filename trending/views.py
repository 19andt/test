import json
from django.http import JsonResponse
from django.views.generic import View
from review_topic.controller import ReviewTopicController
from user.get_user import GetUser


class TrendingListView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            trending_list = ReviewTopicController.GetTrendingTopics(7)
            return JsonResponse({
                'TrendingTopics': trending_list,
                'UserAuthenticated': True
            })
        return JsonResponse({
            'UserAuthenticated': False
        })