from rest_framework import serializers
from timelog.models import User, UserDefault, UserTimeSummary, TimeLogEntry, UserLiveStatus

from timelog.core.base import convert_time_str_to_time_obj, get_time_delta


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
    login_name = serializers.CharField()
    sap_id = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email_id = serializers.EmailField()
    mandatory_break_time = serializers.IntegerField()
    mandatory_working_time_per_day = serializers.IntegerField()
    net_working_hrs = serializers.IntegerField()
    live_date = serializers.DateField(required=False)
    live_time = serializers.TimeField(required=False)
    live_state = serializers.IntegerField(required=False)
    total_work_time = serializers.IntegerField(required=False)

    def create(self, validated_data):
        assert isinstance(
            validated_data, dict), "Invalid type for parameter 'data'"
        login_name = validated_data["login_name"]
        sap_id = validated_data["sap_id"]
        first_name = validated_data["first_name"]
        last_name = validated_data["last_name"]
        email_id = validated_data["email_id"]
        status = validated_data.get("status", 1)
        mandatory_break_time = validated_data.get("mandatory_break_time", 1800)
        mandatory_working_time_per_day = validated_data.get(
            "mandatory_working_time_per_day", 28800)

        net_working_hrs = validated_data.get("net_working_hrs", 0)
        User.objects_include_related.create(login_name, sap_id, first_name, last_name, email_id,
                                            status, mandatory_break_time, mandatory_working_time_per_day, net_working_hrs)


class TimeLogEntrySerializer(serializers.Serializer):
    log_user = serializers.CharField()
    log_date = serializers.DateField()
    log_time = serializers.TimeField()
    log_type = serializers.IntegerField()

    def create(self, validated_data):
        assert isinstance(
            validated_data, dict), "Invalid type for parameter 'data'"
        log_user = validated_data["log_user"]
        log_date = validated_data["log_date"]
        log_time = validated_data["log_time"]
        log_type = validated_data["log_type"]

        user = User.objects.get(login_name=log_user)
        log_entry = TimeLogEntry.objects.create(
            log_user=user, log_date=log_date, log_time=log_time, log_type=log_type)

        log_entry.save()

        # Update live_status based on punch_type
        live_status = UserLiveStatus.objects.get(user=log_user)
        if log_type == 0:
            prev_log_in_time = live_status.time
            log_time_obj = convert_time_str_to_time_obj(log_time)
            interval = get_time_delta(log_time_obj, prev_log_in_time)
            print("Work interval = %s - %s = %s" %
                  (log_time, prev_log_in_time, interval))
        elif log_type == 1:
            interval = 0
        else:
            raise ValueError("Invalid value encountered !")
        live_status.time = log_time
        live_status.state = log_type
        live_status.total_work_time = live_status.total_work_time + interval
        live_status.save()
