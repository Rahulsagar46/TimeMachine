from datetime import date
from timelog.models import User
from timelog.serializers import UserSerializer, UserDataSerializer


def list_all_users():
    user_list = User.objects.all()
    serializer = UserSerializer(user_list, many=True)

    return serializer.data


def get_initial_user_details(user_login):
    try:
        # objects_include_related is a custom manager method for User model to load all related information of User
        user = User.objects_include_related.get(login_name=user_login)
        serializer = UserDataSerializer(user)
        final_json = serializer.data
        status = True
    except User.DoesNotExist:
        status = False
        final_json = None

    return (status, final_json)


def create_new_user_with_relevant_data(user_data):
    serializer = UserDataSerializer(data=user_data)
    is_valid = serializer.is_valid()
    if is_valid:
        new_user = serializer.create(serializer.data)
        return (True, new_user)
    else:
        return (False, serializer.errors)
