from django.conf.urls import url, include
from .views.new_review_image_upload import NewReviewImageUploadView

urlpatterns = [
    # url to upload the images of new review
    url(r'^new_review/image', NewReviewImageUploadView.as_view()),
]