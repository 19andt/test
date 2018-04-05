from django.conf.urls import url, include
from .rest_views import interest_list, interest_detail
from .views.get_comments import GetCommentsView
from .views.add_comment import AddCommentView

urlpatterns = [
    # url to get the comments
    url(r'^get_comments/(?P<review_id>[0-9]+)', GetCommentsView.as_view()),
    # url to add comment
    url(r'^add_comment', AddCommentView.as_view()),

    # rest framework
    url(r'^rest/api/$', interest_list.as_view()),
    url(r'^rest/api/(?P<pk>[0-9]+)/$', interest_detail.as_view()),
]