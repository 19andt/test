from django.conf.urls import url, include
from .rest_views import review_topic_list, review_topic_detail

urlpatterns = [
    # rest framework
    url(r'^rest/api/$', review_topic_list.as_view()),
    url(r'^rest/api/(?P<pk>[0-9]+)/$', review_topic_detail.as_view()),
]