from django.conf.urls import url, include
from .rest_views import subscription_list, subscription_detail
from .views.get_subscription_list import GetSubscriptionListView
from .views.subscription_status import SubscriptionStatusView
from .views.get_observer_count import GetObserverCountView

urlpatterns = [
    # url to get subscriptions
    url(r'^get_subscription_list', GetSubscriptionListView.as_view()),
    # url to get subscription status
    url(r'^subscription_status/(?P<username>[\w -]+)', SubscriptionStatusView.as_view()),
    # url to get subscription count
    url(r'^get_observer_count', GetObserverCountView.as_view()),

    # rest framework
    url(r'^rest/api/$', subscription_list.as_view()),
    url(r'^rest/api/(?P<pk>[0-9]+)/$', subscription_list.as_view()),
]