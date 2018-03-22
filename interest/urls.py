from django.conf.urls import url, include
from .rest_views import interest_list, interest_detail
from .views.get_interests import GetInterestsView
from .views.update_interests import UpdateInterestsView
from .views.edit_interest import EditInterestView

urlpatterns = [
    # url to get the interests
    url(r'^get_interests', GetInterestsView.as_view()),
    # url to update the interests
    url(r'^update_interests', UpdateInterestsView.as_view()),
    # url to get individual interests
    url(r'^edit_interest/(?P<topic_name>[\w -]+)', EditInterestView.as_view()),

    # rest framework
    url(r'^rest/api/$', interest_list.as_view()),
    url(r'^rest/api/(?P<pk>[0-9]+)/$', interest_detail.as_view()),
]