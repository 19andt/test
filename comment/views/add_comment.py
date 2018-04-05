import json
from django.http import JsonResponse
from django.views import View
from comment.serializers import CommentSerializer
from comment.controller import CommentController
from review.controller import ReviewController


class AddCommentView(View):
    def post(self, request, *args, **kwargs):
        # Getting a data from the request
        data = json.loads(request.body.decode('utf-8'))
        # Checking if the user is authenticated
        if request.user.is_authenticated():
            new_comment = {
                'user': request.user,
                'review': ReviewController.GetReviewByID(ID=int(data.get('review_id'))),
                'caption': data.get('caption'),
                'description': data.get('description')
            }

            if CommentController.AddComment(new_comment):
                return JsonResponse({'AddCommentStatus': True, 'UserAuthenticated': True})
            else:
                return JsonResponse({'AddCommentStatus': False, 'UserAuthenticated': True})
        else:
            return JsonResponse({'UserAuthenticated': False})