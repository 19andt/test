"""ReviewBag URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from home.views import HomeView
from ang.views import AngTemplateView
from search.views import SearchTextView
from notification.views import NotificationView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ang/templates/(?P<item>[A-Za-z0-9\_\-\.\/]+)\.html$', AngTemplateView.as_view()),
    url(r'^person/', include('person.urls')),
    url(r'^topic/', include('topic.urls')),
    url(r'^interest/', include('interest.urls')),
    url(r'^subscription/', include('subscription.urls')),
    url(r'^review/', include('review.urls')),
    url(r'^rating/', include('rating.urls')),
    url(r'^rating_detail/', include('rating_detail.urls')),
    url(r'^review_topic/', include('review_topic.urls')),
    url(r'^search', SearchTextView.as_view()),
    url(r'^notification', NotificationView.as_view()),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    url(r'', HomeView.as_view())
]
