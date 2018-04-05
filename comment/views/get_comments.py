import json
from django.http import JsonResponse
from django.views import View
from comment.serializers import CommentSerializer
from comment.controller import CommentController
from review.controller import ReviewController


class GetCommentsView(View):
    def get(self, request, review_id, *args, **kwargs):
        if request.user.is_authenticated():
            qs = CommentController.GetCommments(Review=ReviewController.GetReviewByID(ID=int(review_id)))

            comment_list = []
            for item in qs:
                comment_list.append(CommentSerializer(item).data)
            return JsonResponse({'CommentList': comment_list, 'UserAuthenticated': True})
        else:
            return JsonResponse({'UserAuthenticated': False})