import json
from django.http import JsonResponse
from django.views import View
from topic.controller import TopicController
from topic.serializers import TopicSerializer


class GetTopicView(View):
    def get(self, request, topic_name, *args, **kwargs):
        # Searching for the topic name in the database
        qs = TopicController.GetTopic(Name=topic_name)
        print(topic_name)
        # Returning the result
        if qs.count == 0:
            return JsonResponse({'Topic': None})
        else:
            return JsonResponse({'Topic': TopicSerializer(qs[0]).data})