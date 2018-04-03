from django.db import models
from topic.models import topic
from review.models import review

# Create your models here.


class review_topic(models.Model):
    # Foreign key of the User model
    review=models.ForeignKey(review)
    # Foreign key of the Topic model
    topic=models.ForeignKey(topic)
    # Created timestamp
    created=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        # Name for the row in the database
        return str(self.review.__str__() + ' - ' + self.topic.__str__())