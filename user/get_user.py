from django.contrib.auth.models import User


class GetUser:
    def get_user_by_username(username):
        # Querying for the user
        qs=User.objects.filter(username=username)
        # Checking if the query result count is equal to one
        if qs.count()==1:
            # Returning the query result
            return qs[0]
        else:
            # Returning empty
            return None