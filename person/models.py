import uuid
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from allauth.account.signals import user_signed_up, user_logged_in

# Create your models here.

types = (
    ('I', 'Individual'),
    ('C', 'Company'),
)

genders = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('N', 'Not interested to tell'),
)

def profile_pic_location(instance, filename):
    # Defining the profile pic location
    return 'profile/%s/%s' %(instance.id, filename)

def scramble_uploaded_filename(instance, filename):
    extension = filename.split(".")[-1]
    return "profile/{}.{}".format(uuid.uuid4(), extension)


class person(models.Model):
    # Foreign key of the User model
    user=models.OneToOneField(settings.AUTH_USER_MODEL)
    # Sex of the user
    gender=models.CharField(max_length=1, choices=genders, default='M')
    # Field for the mobile number
    mobile_number=models.CharField(max_length=20)
    # Field about user details
    bio=models.TextField(default='')
    # Type of user
    type=models.CharField(max_length=20, choices=types, default='I')
    # Updated timestamp
    updated=models.DateTimeField(auto_now=True)
    # Profile photo
    pic=models.ImageField(upload_to=scramble_uploaded_filename, null=True, blank=True, width_field='width_field', height_field='height_field')
    # Width of the photo
    width_field=models.IntegerField(default=0)
    # Height of the photo
    height_field=models.IntegerField(default=0)
    # Pic from social_networking site
    pic_url=models.TextField(default='')

    def __str__(self):
        # Name for the row in the database
        return str(self.user.get_full_name())

    @receiver(user_signed_up)
    def user_signed_up_(request, user, sociallogin=None, **kwargs):
        print('New User Signed Up')

        # Making the person object and adding the details to the person object
        new_person = person()
        new_person.user = user

        if sociallogin.account.extra_data.get('picture') != None:
            new_person.pic_url = sociallogin.account.extra_data.get('picture')

        # Saving the person object
        new_person.save()

    @receiver(user_logged_in)
    def user_logged_in(request, user, sociallogin=None, **kwargs):
        print('User Logged In')