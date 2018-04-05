from django.db import models
from review.models import review
from django.conf import settings

# Create your models here.


class comment(models.Model):
    # Foreign key of the user model
    user=models.ForeignKey(settings.AUTH_USER_MODEL)
    # Foreign key of the review model
    review=models.ForeignKey(review)
    # Caption of the comment
    caption=models.CharField(max_length=200, default='')
    # Description of the comment
    description = models.TextField(default='')
    # Timestamp when the row was created
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Name for the row in the database
        return str(self.user.get_full_name() + ' - ' + self.review.__str__())