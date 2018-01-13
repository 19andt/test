from django.db import models
from topic.models import topic
from django.conf import settings

# Create your models here.


class interest(models.Model):
    # Foreign key of the user model
    user=models.ForeignKey(settings.AUTH_USER_MODEL)
    # Foreign key of the topic model
    topic=models.ForeignKey(topic)
    # Timestamp when the row was created
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Name for the row in the database
        return str(self.user.get_full_name() + ' - ' + self.topic.__str__())