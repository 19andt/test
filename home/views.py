from django.shortcuts import render, render_to_response
from django.views import View


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')