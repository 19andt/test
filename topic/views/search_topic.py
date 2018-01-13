import json
from django.http import JsonResponse
from django.views import View
from topic.controller import TopicController
from topic.serializers import TopicSerializer


class SearchTopicView(View):
    def post(self, request, *args, **kwargs):
        # Getting the data from the request
        data=json.loads(request.body.decode('utf-8'))
        topic_list=[]
        # Getting the topics from the controller and appending it to the list
        for item in TopicController.GetTopics(Name=data.get('topic_name')):
            topic_list.append(item)
        # Returning the list
        return JsonResponse({'TopicList': topic_list})