import os
import json
from django.http import JsonResponse
from django.views.generic import View
from topic.controller import TopicController
from user.get_user import GetUser


class SearchTextView(View):
    def post(self, request, *args, **kwargs):
        # Getting the data from the request
        data = json.loads(request.body.decode('utf-8'))
        print(data)

        user_list = []
        # Getting the users from the controller and appending it to the list
        for item in GetUser.get_users(Name=data.get('search_text'))[:5]:
            user_list.append(item)

        topic_list = []
        # Getting the topics from the controller and appending it to the list
        for item in TopicController.GetTopics(Name=data.get('search_text'))[:5]:
            topic_list.append(item)
        return JsonResponse({
            'SearchingFor': data.get('search_text'),
            'TopicList': topic_list,
            'UserList': user_list
        })