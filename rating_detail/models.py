from django.db import models
from django.conf import settings
from topic.models import topic

# Create your models here.


class rating_detail(models.Model):
    # Foreign key of the User model
    user=models.ForeignKey(settings.AUTH_USER_MODEL)
    # Foreign key of the Topic model
    topic=models.ForeignKey(topic)
    # Number of ratings with rating equal to one
    one=models.PositiveIntegerField(default=0)
    # Number of ratings with rating equal to two
    two=models.PositiveIntegerField(default=0)
    # Number of ratings with rating equal to three
    three=models.PositiveIntegerField(default=0)
    # Number of ratings with rating equal to four
    four=models.PositiveIntegerField(default=0)
    # Number of ratings with rating equal to five
    five=models.PositiveIntegerField(default=0)

    def __str__(self):
        # Name for the row in the database
        return str(self.user.get_full_name() + ' - ' + self.topic.__str__() + ' - ' + int(self.one + self.two + self.three + self.four + self.five))