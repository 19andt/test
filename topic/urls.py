from django.conf.urls import url, include
from .rest_views import topic_list, topic_detail
from .views.search_topic import SearchTopicView
from .views.get_topic import GetTopicView
from .views.update_topic import UpdateTopicView

urlpatterns = [
    # url for getting the topics
    url(r'^search_topic$', SearchTopicView.as_view()),
    url(r'^get_topic/(?P<topic_name>[\w -]+)', GetTopicView.as_view()),
    url(r'^update_topic$', UpdateTopicView.as_view()),

    # rest framework
    url(r'^rest/api/$', topic_list.as_view()),
    url(r'^rest/api/(?P<pk>[0-9]+)/$', topic_detail.as_view()),
]