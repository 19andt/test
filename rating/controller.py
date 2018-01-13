from django.db.models import Sum
from .models import rating


class RatingController:

    def GetRating(Person, Review):
        # Making a dictionary for the rating data
        rating_data={}

        # Querying the data base for rating for the review by the person
        qs=rating.objects.filter(user=Person, review=Review)
        if qs.count()==1:
            # Adding the personal rating data
            rating_data['personal_rating']=int(qs[0].value)
        else:
            # Adding the personal rating data as 0
            rating_data['personal_rating']=int(0)

        # Querying the ratings for different values and adding the sum of all the values to the dictionary
        qs=rating.objects.filter(review=Review)
        rating_data['1']=qs.filter(value=1).aggregate(Sum('value')).get('value__sum')
        rating_data['2']=qs.filter(value=2).aggregate(Sum('value')).get('value__sum')
        rating_data['3']=qs.filter(value=3).aggregate(Sum('value')).get('value__sum')
        rating_data['4']=qs.filter(value=4).aggregate(Sum('value')).get('value__sum')
        rating_data['5']=qs.filter(value=5).aggregate(Sum('value')).get('value__sum')

        # Returning the rating data
        return rating_data


    def UpdateRating(Person, Review, RatingValue):
        # Querying for the rating objects
        qs = rating.objects.filter(user=Person, review=Review)
        # Checking if the query result count has a value of one
        if qs.count()==1:
            # Update the rating object and it will automatically save
            qs.update(value=RatingValue)
            # for obj in qs:
            #     obj.value=RatingValue
            #     print(obj.value)
            #     obj.save()
        else:
            # Creating a new rating object and adding the parameters
            new_rating=rating.objects.create(
                review=Review,
                user=Person,
                value=RatingValue
            )
            # Saving the new rating object
            new_rating.save()
        return True