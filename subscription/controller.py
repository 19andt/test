from .models import subscription


class SubscriptionController:

    def GetSubscriptions(User):
        # Getting the subscriptions for a particular user
        return subscription.objects.filter(observer=User)