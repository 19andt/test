from .models import comment


class CommentController:

    def GetCommments(Review):
        if Review == None:
            return None
        return comment.objects.filter(review=Review).order_by('created')

    def AddComment(Data):
        new_comment = comment.objects.create(
            user=Data.get('user'),
            review=Data.get('review'),
            caption=Data.get('caption'),
            description=Data.get('description')
        )

        new_comment.save()

        return True