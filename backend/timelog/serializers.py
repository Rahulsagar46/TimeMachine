from rest_framework import serializers
from timelog.models import User, UserDefaults


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['unique_id', 'first_name',
                  'last_name', 'email_id', 'login_name']


class UserDefaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDefaults
        fields = ['user_id', 'mandatory_break_time',
                  'mandatory_working_time_per_day']
