from django.conf.urls import url, include
from .rest_views import topic_list, topic_detail
from .views.search_topic import SearchTopicView

urlpatterns = [
    # url for getting the topics
    url(r'^search_topic$', SearchTopicView.as_view()),

    # rest framework
    url(r'^rest/api/$', topic_list.as_view()),
    url(r'^rest/api/(?P<pk>[0-9]+)/$', topic_detail.as_view()),
]