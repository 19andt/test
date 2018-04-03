from collections import Counter
from datetime import datetime, timedelta
from .models import review_topic
from topic.controller import TopicController


class ReviewTopicController:

    def GetReviews(Topic):
        # Getting the reviews for a topic
        return review_topic.objects.filter(topic=Topic)

    def GetTopics(Review):
        # Getting the topics associated with the review
        qs = review_topic.objects.filter(review = Review)

        topic_list = []
        for item in qs:
            topic_list.append(item.topic.name)

        return topic_list

    def AddTopics(Review, TopicsList):
        # Adding the topics to the review
        for topic in TopicsList:
            # Creating a new row for the review and the topic
            new_review_topic = review_topic.objects.create(
                review=Review,
                topic=topic
            )
            # Saving the row
            new_review_topic.save()
        return True

    def GetTrendingTopics(days):
        time_threshold = datetime.now() - timedelta(days=days)
        print(time_threshold)
        topics = review_topic.objects.values('topic').filter(created__gt=time_threshold)

        topic_list = []
        for topic in topics:
            topic_list.append(TopicController.GetTopic(ID=topic.get('topic'))[0].name)

        topic_list = [[i, j] for i, j in Counter(topic_list).most_common()[:10]]
        return topic_list