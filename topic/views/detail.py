import json, uuid
from django.http import JsonResponse
from django.views import View
from topic.controller import TopicController
from topic.serializers import TopicSerializer
from django.core.files.storage import FileSystemStorage


class DetailView(View):
    def get(self, request, topic_name, *args, **kwargs):
        # Searching for the topic name in the database
        qs = TopicController.GetTopic(Name=topic_name)
        print(topic_name)
        # Returning the result
        if qs.count == 0:
            return JsonResponse({'Topic': None})
        else:
            return JsonResponse({'Topic': TopicSerializer(qs[0]).data})

    def post(self, request, topic_name, *args, **kwargs):
        try:
            # Getting the data from the request
            data=json.loads(request.body.decode('utf-8'))
        except:
            data = {}
        if request.user.is_authenticated():
            # Getting the topic from the controller
            qs = TopicController.GetTopic(Name=topic_name)
            if qs.count() != 0:
                current_topic = qs[0]
                if data.get('description') != None:
                    # Updating the description
                    current_topic.description = data.get('description')

                # Procedure for storing images
                if request.FILES.get('pic') != None:
                    pic = request.FILES.get('pic')
                    fs = FileSystemStorage()
                    filename = fs.save('topic/' + str(uuid.uuid4()) + '.' + pic.name.split('.')[-1], pic)
                    uploaded_file_url = fs.url(filename)
                    current_topic.pic = uploaded_file_url[7:]
                # Save topic
                current_topic.save()
                # Returning the list
                return JsonResponse({'UpdateStatus': True})
            else:
                return JsonResponse({'UpdateStatus': False})
        else:
            return JsonResponse({'UpdateStatus': False})