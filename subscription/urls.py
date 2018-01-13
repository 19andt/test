from django.conf.urls import url, include
from .rest_views import subscription_list, subscription_detail

urlpatterns = [
    # rest framework
    url(r'^rest/api/$', subscription_list.as_view()),
    url(r'^rest/api/(?P<pk>[0-9]+)/$', subscription_list.as_view()),
]