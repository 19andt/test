import os
from django.conf import settings
from django.http import HttpResponse, Http404
from django.views.generic import View


class AngTemplateView(View):
    def get(self, request, item=None, *args, **kwargs):
        # Getting the template folder from the settings file
        template_dir_path = settings.TEMPLATES[0]["DIRS"][0]
        # Calculating the final path of the html file
        final_path = os.path.join(template_dir_path, 'ang', item + '.html')
        try:
            # Opening the html file
            html = open(final_path)
            # Returning the text of the html file
            return HttpResponse(html)
        except:
            # Returning the 404 error
            raise Http404