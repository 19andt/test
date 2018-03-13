import json
from django.http import JsonResponse
from django.views import View
from topic.controller import TopicController
from topic.serializers import TopicSerializer


class UpdateTopicView(View):
    def post(self, request, *args, **kwargs):
        # Getting the data from the request
        data=json.loads(request.body.decode('utf-8'))
        print(data)
        # Getting the topic from the controller
        qs = TopicController.GetTopic(Name=data.get('topic_name'))
        topic = qs[0]
        print(topic)
        # Updating the description
        setattr(topic, 'description', data.get('description'))
        # Save topic
        topic.save()
        # Returning the list
        return JsonResponse({'UpdateStatus': True})