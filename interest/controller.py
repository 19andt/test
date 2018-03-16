from .models import interest
from topic.controller import TopicController


class InterestController:

    def GetInterests(User):
        # Getting the interests for a user
        return interest.objects.filter(user=User)

    def UpdateInterests(User, Data):
        # Getting the interests for the user
        qs=interest.objects.filter(user=User)
        # Converting the query results into a list
        qs_list=list(qs)
        # Printing the query set
        print(qs_list)
        # Looping through each item in the Data
        for item in Data:
            # Checking if the interest was previously added
            if item['type']=='old':
                # Filtering the query set for the topic name and the topic is not present
                if qs.filter(topic__name=item['text']).count()==0:
                    # Creating a new object of interest and adding the parameters
                    new_interest=interest.objects.create(
                        user=User,
                        topic=TopicController.GetTopic(Name=item['text'])[0]
                    )
                    # Saving the interest object
                    new_interest.save()
                # Filtering th equery set for the topic name and topic is present
                elif qs.filter(topic__name=item['text']).count()==1:
                    # Removing the item from the query set and *not from the database*
                    print('Removing')
                    print(item)
                    qs_list.remove(list(qs.filter(topic__name=item['text']))[0])
                    # Printing the query set
                    print(qs_list)
            # Checking if interest is newly added by the user
            elif item['type']=='new':
                # Making a dictionary for the topic parameters
                topic_data={
                    'name': item['text'],
                    'added_by': User,
                    'description': ''
                }
                # Adding the new topic into the database
                if TopicController.AddTopic(Data=topic_data):
                    # Creating a new object for the interest and adding the parameters
                    new_interest=interest.objects.create(
                        user=User,
                        topic=TopicController.GetTopic(Name=item['text'])[0]
                    )
                    # Saving the interest
                    new_interest.save()
        # Deleting the unused item from the database
        for item in qs_list:
            item.delete()
        # Returning
        return

    def AddInterests(User, Data):
        for item in Data:
            if item['type'] == 'new':
                topic_data = {
                    'name': item['text'],
                    'added_by': User,
                    'description': ''
                }
                if TopicController.AddTopic(Data=topic_data):
                    # Creating a new object for the interest and adding the parameters
                    new_interest=interest.objects.create(
                        user=User,
                        topic=TopicController.GetTopic(Name=item['text'])[0]
                    )
                    # Saving the interest
                    new_interest.save()
            else:
                # Creating a new object for the interest and adding the parameters
                new_interest = interest.objects.create(
                    user=User,
                    topic=TopicController.GetTopic(Name=item['text'])[0]
                )
                # Saving the interest
                new_interest.save()
        return