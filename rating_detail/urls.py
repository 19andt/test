from django.conf.urls import url, include
from .rest_views import rating_detail_list, rating_detail_detail

urlpatterns = [
    # rest framework
    url(r'^rest/api/$', rating_detail_list.as_view()),
    url(r'^rest/api/(?P<pk>[0-9]+)/$', rating_detail_detail.as_view()),
]