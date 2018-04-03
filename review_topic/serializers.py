from rest_framework import serializers
from .models import review_topic
from review.serializers import ReviewSerializer
from topic.serializers import TopicSerializer


class RatingTopicSerializer(serializers.ModelSerializer):
    # Defining the serializer for the foreign key
    review=ReviewSerializer()
    topic=TopicSerializer()

    class Meta:
        # Defining the serializer for the foreign key
        model=review_topic
        # Defining the serializer for the foreign key
        fields=('id', 'review', 'topic', 'created')