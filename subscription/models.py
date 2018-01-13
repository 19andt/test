from django.db import models
from django.conf import settings

# Create your models here.


class subscription(models.Model):
    # Foreign key of the user model *observer*
    observer=models.ForeignKey(settings.AUTH_USER_MODEL, related_name='observer')
    # Foreign key of the user model *reviewer*
    reviewer=models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reviewer')
    # Timestamp when the row was created
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Name for the row in the database
        return str('o:' + ' - ' + self.observer.get_full_name() + ' r:' + ' - ' + self.reviewer.get_full_name())