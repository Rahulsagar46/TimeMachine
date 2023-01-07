from datetime import datetime
from rest_framework import serializers
from timelog.models import User, UserDefault, UserTimeSummary, TimeLogEntry, UserLiveStatus, UserTimeRecord

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
    net_working_time = serializers.IntegerField()
    last_update = serializers.DateTimeField(required=False)
    live_state = serializers.IntegerField(required=False)

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

        net_working_time = validated_data.get("net_working_time", 0)
        User.objects_include_related.create(login_name, sap_id, first_name, last_name, email_id,
                                            status, mandatory_break_time, mandatory_working_time_per_day, net_working_time)


class TimeLogEntrySerializer(serializers.Serializer):
    log_user = serializers.CharField()
    log_date = serializers.DateField()
    log_in_time = serializers.TimeField(required=False)
    log_out_time = serializers.TimeField(required=False)
    log_state = serializers.IntegerField()

    def create(self, validated_data):
        assert isinstance(
            validated_data, dict), "Invalid type for parameter 'data'"
        log_user = validated_data["log_user"]
        log_date = validated_data["log_date"]
        log_in_time = validated_data.get("log_in_time", None)
        log_out_time = validated_data.get("log_out_time", None)
        log_state = validated_data["log_state"]

        user = User.objects_include_related.get(login_name=log_user)

        todays_time_record = UserTimeRecord.objects.filter(
            user=user, date=log_date)
        if todays_time_record.count() == 0:
            user_time_record = UserTimeRecord.objects.create(user=user, date=log_date, mandatory_work_time=user.mandatory_working_time_per_day,
                                                             mandatory_break_time=user.mandatory_break_time, total_work_time_for_day=0)
        else:
            assert todays_time_record.count(
            ) == 1, "FATAL error! Multiple time records per day for user"
            user_time_record = todays_time_record.get()

        if user.userlivestatus.active_log == -1:
            assert log_out_time == None, "Invalid data"
            log_entry = TimeLogEntry.objects.create(
                log_user=user, log_date=log_date, log_in_time=log_in_time, log_out_time=log_out_time, log_state=log_state)
            log_entry.save()
            log_time = log_in_time
            user_time_record.log_entries.add(log_entry)
            user_time_record.save()
            live_state = 1
            active_log_id = log_entry.pk
        else:
            log_entry = TimeLogEntry.objects.get(
                pk=user.userlivestatus.active_log)
            log_time = log_out_time
            assert log_entry.log_state == 0, "LOG entry must be unsettled at this point"
            assert log_in_time not in validated_data, "processing error"

            time_interval = get_time_delta(
                convert_time_str_to_time_obj(log_out_time), log_entry.log_in_time)

            log_entry.log_out_time = log_out_time
            log_entry.log_state = 1
            log_entry.save()

            # Update the total working time in the interval in user_time_record
            user_time_record.total_work_time_for_day = user_time_record.total_work_time_for_day + time_interval
            user_time_record.save()

            live_state = 0
            active_log_id = -1

        # update live status
        user.userlivestatus.live_state = live_state
        user.userlivestatus.active_log = active_log_id
        user.userlivestatus.last_update = datetime.now()
        user.userlivestatus.save()
