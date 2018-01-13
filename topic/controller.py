from .models import topic


class TopicController:

    def GetTopics(Name):
        # Returning the topics with the similar name
        return topic.objects.values_list('name', flat=True).filter(name__icontains=Name)

    def GetTopic(Name=None, ID=None):
        # Querying the topics by name
        if Name!=None and ID==None:
            # Returning the topics
            return topic.objects.filter(name=Name)
        # Querying the topics by ID
        elif Name==None and ID!=None:
            # Returning the topics
            return topic.objects.filter(id=ID)

    def AddTopic(Data):
        # Creating a new topic object and adding the values to columns
        new_topic=topic.objects.create(
            name=Data.get('name'),
            added_by=Data.get('added_by'),
            description=Data.get('description')
        )
        # Saving the topic
        new_topic.save()
        return True

    def CheckTopicExists(Name):
        # Querying for the topic name
        topic_count=topic.objects.filter(name=Name).count()
        # Checking if the count for the topic is equal to one
        if topic_count==1:
            # Returning true
            return True
        else:
            # Returning false
            return False