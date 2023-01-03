from rest_framework import serializers
from timelog.models import User, UserDefault, UserTimeSummary, TimeLogEntry, UserLiveStatus


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
    live_state = serializers.IntegerField()
    total_work_time = serializers.IntegerField()

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
        live_status.state = log_type
        live_status.save()
