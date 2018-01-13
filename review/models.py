from django.db import models
from django.conf import settings
from topic.models import topic

# Create your models here.


def review_pic_location(instance, filename):
    # Defining the profile pic location
    return 'review/%s/%s' %(instance.id, filename)


class review(models.Model):
    # Foreign key of the User model
    added_by=models.ForeignKey(settings.AUTH_USER_MODEL)
    # # Foreign key of the Topic model
    # topic=models.ForeignKey(topic)
    # Caption of the review
    caption=models.CharField(max_length=200)
    # Briefing of the review
    briefing=models.TextField(default='')
    # User rating of the review
    review_rating=models.IntegerField(default=0)
    # Created timestamp
    created=models.DateTimeField(auto_now_add=True)
    # Updated timestamp
    updated=models.DateTimeField(auto_now=True)
    # Picture added to the review
    pic=models.ImageField(upload_to=review_pic_location, null=True, blank=True, width_field='width_field', height_field='height_field')
    # Width of the picture
    width_field=models.IntegerField(default=0)
    # Height of the picture
    height_field=models.IntegerField(default=0)

    def __str__(self):
        # Name for the row in the database
        return str(self.added_by.get_full_name() + ' - ' + self.caption)