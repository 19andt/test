from django.db import models
from django.conf import settings

# Create your models here.
def scramble_uploaded_filename(instance, filename):
    extension = filename.split(".")[-1]
    return "profile/{}.{}".format(uuid.uuid4(), extension)


class topic(models.Model):
    # Name of the topic
    name=models.CharField(max_length=200)
    # User who added the topic
    added_by=models.ForeignKey(settings.AUTH_USER_MODEL)
    # Timestamp at which the topic was added
    timestamp=models.DateTimeField(auto_now_add=True)
    # Description of the topic
    description=models.TextField(default='')
    # Profile photo
    pic = models.ImageField(upload_to=scramble_uploaded_filename, null=True, blank=True, width_field='width_field',height_field='height_field')
    # Width of the photo
    width_field = models.IntegerField(default=0)
    # Height of the photo
    height_field = models.IntegerField(default=0)

    def __str__(self):
        # Name for the row in the database
        return str(self.name)