from .models import subscription


class SubscriptionController:

    def GetSubscriptions(User):
        # Getting the subscriptions for a particular user
        return subscription.objects.filter(observer=User)

    def GetSubscription(Observer, Reviewer):
        # Getting the subscriptions
        return subscription.objects.filter(observer=Observer, reviewer=Reviewer)

    def AddSubscription(Observer, Reviewer):
        qs = subscription.objects.filter(observer=Observer, reviewer=Reviewer)
        if qs.count() == 0:
            # Creating a new topic object and adding the values to columns
            new_subscription = subscription.objects.create(
                observer=Observer,
                reviewer=Reviewer
            )

            # Saving the subscription
            new_subscription.save()
        return True

    def DeleteSubscription(Observer, Reviewer):
        subscription.objects.filter(observer=Observer, reviewer=Reviewer).delete()
        return True

    def GetObservers(User):
        # Getting the observers for the user
        return subscription.objects.filter(reviewer=User)