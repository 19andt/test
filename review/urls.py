from django.conf.urls import url, include
from .rest_views import review_list, review_detail
from .views.get_reviews_user import GetReviewsUserView
from .views.get_reviews_topic import GetReviewsTopicView
from .views.add_review import AddReviewView
from .views.get_review import GetReviewView

urlpatterns = [
    # url to get the reviews by the user
    url(r'^get_reviews_user', GetReviewsUserView.as_view()),
    # url to get the reviews by the topic
    url(r'^get_reviews_topic/(?P<topic_name>[\w -]+)', GetReviewsTopicView.as_view()),
    # url to add the review
    url(r'^add_review', AddReviewView.as_view()),
    # url to get a single review
    url(r'^get_review/(?P<id>[0-9]+)', GetReviewView.as_view()),

    # rest framework
    url(r'^rest/api/$', review_list.as_view()),
    url(r'^rest/api/(?P<pk>[0-9]+)/$', review_detail.as_view()),
]