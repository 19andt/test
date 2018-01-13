from django.conf.urls import url, include
from .rest_views import rating_list, rating_detail
from .views.update_rating import UpdateRatingView

urlpatterns = [
    # url to update the rating
    url(r'^update_rating', UpdateRatingView.as_view()),

    # rest framework
    url(r'^rest/api/$', rating_list.as_view()),
    url(r'^rest/api/(?P<pk>[0-9]+)/$', rating_detail.as_view()),
]