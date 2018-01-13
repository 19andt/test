from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from review.models import review

# Create your models here.


class rating(models.Model):
    # Foreign key of the Review model
    review=models.ForeignKey(review)
    # Foreign key of the User model
    user=models.ForeignKey(settings.AUTH_USER_MODEL)
    # Value of the rating
    value=models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        # Name for the row in the database
        return str(self.user.get_full_name() + ' - ' + self.review.__str__() + ' - ' + str(self.value))