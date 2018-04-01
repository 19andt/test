import json, uuid
from django.http import JsonResponse
from django.views import View

class NewReviewImageUploadView(View):
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            print(request.FILES)
        return JsonResponse({})