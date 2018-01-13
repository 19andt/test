from django.conf.urls import url, include
from .views.add_user import AddUserView
from .views.login import LoginView
from .views.logout import LogoutView
from .views.check_authentication import CheckAuthenticationView
from .views.person_detail import PersonDetailView
from .rest_views import person_list, person_detail

urlpatterns = [
    # url for getting the person detail
    url(r'get_detail/(?P<username>[\w-]+)', PersonDetailView.as_view()),
    # url for checking authentication
    url(r'check_authentication$', CheckAuthenticationView.as_view()),
    # url for adding the user
    url(r'add_user$', AddUserView.as_view()),
    # url for logging in the user
    url(r'login', LoginView.as_view()),
    # url for logging out the user
    url(r'logout', LogoutView.as_view()),

    # rest framework
    url(r'^rest/api/$', person_list.as_view()),
    url(r'^rest/api/(?P<pk>[0-9]+)/$', person_detail.as_view()),
]