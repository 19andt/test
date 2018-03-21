from django.http import JsonResponse
from .models import review
from interest.controller import InterestController
from subscription.controller import SubscriptionController
from rating.controller import RatingController
from review_topic.controller import ReviewTopicController
from topic.controller import TopicController
from .serializers import ReviewSerializer


class ReviewController:

    def GetReviewsByUser(User):
        # Getting the review added by the user
        return review.objects.filter(added_by=User)

    def GetReviewsByTopic(Topic):
        # Getting the reviews for a topic
        qs = ReviewTopicController.GetReviews(Topic=Topic)

        review_list=[]
        for item in qs:
            review_list.append(item.review)
        return review_list

    def GetReviewsForUser(User):
        # Getting the interests for the user
        interests=InterestController.GetInterests(User=User)
        # Getting the subscription for the user
        subscriptions=SubscriptionController.GetSubscriptions(User=User)

        # Making an empty list of reviews
        reviews=[]

        # Appending the reviews added by the user to the list
        # reviews.extend(list(ReviewController.GetReviewsByUser(User=User)))

        # Appending the reviews by the interest to the list
        for interest in interests:
            reviews.extend(list(ReviewController.GetReviewsByTopic(Topic=interest.topic)))

        # Appending the reviews by the subscriptions to the list
        for subscription in subscriptions:
            reviews.extend(list(ReviewController.GetReviewsByUser(User=subscription.reviewer)))

        # Making a dictionary of reviews with ID as a key
        dictionary={}

        # Looping through each object in the review list
        for obj in reviews:
            dictionary[obj.pk]=obj

        # Retrieving unique reviews from the dictionary
        reviews=dictionary.values()

        # Making a dictionary for the review and the rating information
        derived_list={}

        # Looping through each item in the unique review list
        for index, review_item in enumerate(sorted(reviews, key=lambda x: x.created)[::-1]):
            # Adding a dictionary object with the int as key and review and rating data as a part of another dictionary
            derived_list[index]={
                'review': ReviewSerializer(review_item).data,
                'rating': RatingController.GetRating(Person=User, Review=review_item),
                'topic_list': ReviewTopicController.GetTopics(Review=review_item)
            }

        # Returning the derived list
        return derived_list

    def GetReviewsForTopic(Topic, User):
        # Getting the reviews for a topic from the review controller
        reviews=list(ReviewController.GetReviewsByTopic(Topic=Topic))

        # Making a dictionary for the review and the rating information
        derived_list={}

        # Looping through each item in the review list
        for index, review_item in enumerate(sorted(reviews, key=lambda x: x.created)[::-1]):
            # Adding a dictionary object with the int as key and review and rating data as a part of another dictionary
            derived_list[index]={
                'review': ReviewSerializer(review_item).data,
                'rating': RatingController.GetRating(Person=User, Review=review_item),
                'topic_list': ReviewTopicController.GetTopics(Review=review_item)
            }

        # Returning the derived list
        return derived_list

    def AddReview(Data):
        # Creating a new review object and adding the parameters
        new_review=review.objects.create(
            added_by=Data.get('added_by'),
            caption=Data.get('caption'),
            briefing=Data.get('briefing'),
            # review_rating=Data.get('review_rating'),
            # pic=Data.get('pic')
        )
        # Saving the new review
        new_review.save()

        print(Data)
        InterestController.AddInterests(Data.get('added_by'), Data.get('topic_list'))

        review_topics = []
        for item in Data.get('topic_list'):
            review_topics.append(TopicController.GetTopic(Name=item.get('text'))[0])

        print(review_topics)
        ReviewTopicController.AddTopics(new_review, review_topics)
        return True

    def GetReviewByID(ID):
        # Querying for the reviews by ID
        qs=review.objects.filter(id=ID)
        # Checking if the query set count is zero
        if qs.count()==0:
            # Returning no review
            return None
        else:
            # Retuning the review got from the query set
            return qs[0]