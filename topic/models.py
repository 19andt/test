from django.db import models
from django.conf import settings

# Create your models here.


class topic(models.Model):
    # Name of the topic
    name=models.CharField(max_length=200)
    # User who added the topic
    added_by=models.ForeignKey(settings.AUTH_USER_MODEL)
    # Timestamp at which the topic was added
    timestamp=models.DateTimeField(auto_now_add=True)
    # Description of the topic
    description=models.TextField(default='')

    def __str__(self):
        # Name for the row in the database
        return str(self.name)