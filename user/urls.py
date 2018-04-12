from django.conf.urls import url, include
from .rest_views import user_list, user_detail
from .views.get_logged_in_user import  GetLoggedInUserView

urlpatterns = [
    # url for getting the logged user
    url(r'^get_logged_in_user', GetLoggedInUserView.as_view()),

    # rest framework
    url(r'^rest/api/$', user_list.as_view()),
    url(r'^rest/api/(?P<pk>[0-9]+)/$', user_detail.as_view()),
]