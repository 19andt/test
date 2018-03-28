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

    def get_user_by_email(email):
        # Querying for the user
        qs = User.objects.filter(email=email)
        # Checking if the query result count is equal to one
        if qs.count()==1:
            # Returning the query result
            return qs[0]
        else:
            # Returning empty
            return None

    def get_user_by_id(ID):
        # Querying for the user
        qs = User.objects.filter(id=ID)
        # Checking if the query result count is equal to one
        if qs.count() == 1:
            # Returning the query result
            return qs[0]
        else:
            # Returning empty
            return None

    def get_users(Name):
        # Returning the topics with the similar name
        return User.objects.values('first_name', 'username').filter(first_name__icontains=Name)