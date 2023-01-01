from rest_framework import serializers
from timelog.models import User, UserDefault, UserTimeSummary


class UserDefaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDefault
        fields = ['mandatory_break_time',
                  'mandatory_working_time_per_day']


class UserTimeSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTimeSummary
        fields = ['net_working_hrs']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['sap_id', 'first_name',
                  'last_name', 'email_id', 'login_name']


class UserDataSerializer(serializers.Serializer):
    # custom serializer for sending initial load data for front end
    sap_id = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email_id = serializers.CharField()
    login_name = serializers.CharField()
    mandatory_break_time = serializers.IntegerField()
    mandatory_working_time_per_day = serializers.IntegerField()
    net_working_hrs = serializers.IntegerField()
