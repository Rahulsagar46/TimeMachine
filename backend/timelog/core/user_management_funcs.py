from timelog.models import User, UserDefaults
from timelog.serializers import UserSerializer, UserDefaultSerializer


def list_all_users():
    user_list = User.objects.all()
    serializer = UserSerializer(user_list, many=True)

    return serializer.data


def get_initial_user_details(user_login):
    try:
        user_data = User.objects.get(login_name=user_login)
        user_defaults = UserDefaults.objects.get(user_id=user_data.unique_id)
        serializer1 = UserSerializer(user_data)
        serializer2 = UserDefaultSerializer(user_defaults)
        final_json = {
            "main": serializer1.data,
            "defaults": serializer2.data
        }
        status = True
    except User.DoesNotExist:
        status = False
        final_json = None

    return (status, final_json)
