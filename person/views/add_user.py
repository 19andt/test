import json, random,string
from django.http import JsonResponse
from django.views import View
from django.contrib import auth
from person.models import person
from user.get_user import GetUser


class AddUserView(View):
    def post(self, request, *args, **kwargs):
        # Getting the data from the request
        data=json.loads(request.body.decode('utf-8'))
        user=auth.get_user_model()

        if GetUser.get_user_by_email(email=data.get('email')) != None:
            return JsonResponse({'AddUserStatus': False})

        # Making the new user object
        new_user=user.objects.create(
            first_name=data.get('full_name'),
            email=data.get('email'),
            username=self.CreateShortcode(user)
        )

        # Setting the password for the new user
        new_user.set_password(data.get('password'))

        # Saving the new user
        new_user.save()

        # Making the person object and adding the details to the person object
        new_person=person()
        new_person.user=new_user
        new_person.mobile_number=data.get('mobile_number')

        # Saving the person object
        new_person.save()

        # Logging in the new user
        auth.login(request, new_user)

        # Returning a response
        return JsonResponse({'AddUserStatus': True, 'Login': True})

    def CodeGenerator(self, size=10, chars=string.ascii_letters + string.digits):
        # Generating a random code for the person and returning it
        return ''.join(random.choice(chars) for _ in range(size))

    def CreateShortcode(self, instance, size=10):
        # Creating a random code
        new_code = self.CodeGenerator(size=size)
        # model = instance.__class__
        # qs_exists = model.objects.filter(shortcode=new_code).count()
        # if qs_exists > 1:
        #     return self.CreateShortcode(instance)
        return new_code