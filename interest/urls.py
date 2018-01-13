from django.conf.urls import url, include
from .rest_views import interest_list, interest_detail
from .views.get_interest import GetInterestView
from .views.update_interest import UpdateInterestView

urlpatterns = [
    # url to get the interest
    url(r'^get_interest', GetInterestView.as_view()),
    # url to update the interest
    url(r'^update_interest', UpdateInterestView.as_view()),


    # rest framework
    url(r'^rest/api/$', interest_list.as_view()),
    url(r'^rest/api/(?P<pk>[0-9]+)/$', interest_detail.as_view()),
]