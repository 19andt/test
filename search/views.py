import os
import json
from django.http import JsonResponse
from django.views.generic import View
from topic.controller import TopicController
# from src.ReviewBag.person.controller import


class SearchTextView(View):
    def post(self, request, *args, **kwargs):
        # Getting the data from the request
        data = json.loads(request.body.decode('utf-8'))
        print(data)

        topic_list = []
        # Getting the topics from the controller and appending it to the list
        for item in TopicController.GetTopics(Name=data.get('search_text')):
            topic_list.append(item)
        return JsonResponse({
            'SearchingFor': data.get('search_text'),
            'TopicList': topic_list
        })