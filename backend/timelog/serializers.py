from datetime import datetime
from rest_framework import serializers
from timelog.models import User, UserDefault, UserTimeSummary, TimeLogEntry, UserTimeRecord
from timelog.models import Department, Team, TimeLogCorrectionRequest, Holiday, Vacation, ConflictGroup

from timelog.core.base import get_time_delta, get_time_entry_bounds_for_correction, is_time_within_bounds, get_day_from_number


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
    department = serializers.CharField(required=False)
    team = serializers.CharField(required=False)
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
        department = validated_data.get("department", None)
        team = validated_data.get("team", None)
        mandatory_break_time = validated_data.get("mandatory_break_time", 1800)
        mandatory_working_time_per_day = validated_data.get(
            "mandatory_working_time_per_day", 28800)

        net_working_time = validated_data.get("net_working_time", 0)
        if department != None:
            dept_obj = Department.objects.get(pk=department)
        if team != None:
            team_obj = Team.objects.get(pk=team)
        User.objects_include_related.create(login_name, sap_id, first_name, last_name, email_id,
                                            status, mandatory_break_time, mandatory_working_time_per_day, net_working_time, dept_obj, team_obj)


class TimeLogEntrySerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    log_user = serializers.CharField()
    log_year = serializers.IntegerField()
    log_month = serializers.IntegerField()
    log_day = serializers.IntegerField()
    log_date = serializers.DateField()
    log_in_time = serializers.TimeField(required=False)
    log_out_time = serializers.TimeField(required=False)
    log_state = serializers.IntegerField()
    interval_time = serializers.IntegerField(required=False)

    def create(self, validated_data):
        assert isinstance(
            validated_data, dict), "Invalid type for parameter 'data'"
        log_user = validated_data["log_user"]
        log_year = validated_data["log_year"]
        log_month = validated_data["log_month"]
        log_day = validated_data["log_day"]
        log_date = validated_data["log_date"]
        log_in_time = validated_data.get("log_in_time", None)
        log_out_time = validated_data.get("log_out_time", None)
        log_state = validated_data["log_state"]

        user = User.objects_include_related.get(login_name=log_user)

        week_day_number = datetime.strptime(log_date, '%Y-%m-%d').weekday()
        week_day = get_day_from_number(week_day_number)

        todays_time_record = UserTimeRecord.objects.filter(
            user=user, date=log_date)
        if todays_time_record.count() == 0:
            user_time_record = UserTimeRecord.objects.create(user=user, year=log_year, month=log_month, day=log_day, week_day=week_day, date=log_date, mandatory_work_time=user.mandatory_working_time_per_day,
                                                             mandatory_break_time=user.mandatory_break_time, total_work_time_for_day=0)
        else:
            assert todays_time_record.count(
            ) == 1, "FATAL error! Multiple time records per day for user"
            user_time_record = todays_time_record.get()

        if user.userlivestatus.active_log == -1:
            assert log_out_time == None, "Invalid data"
            log_entry = TimeLogEntry.objects.create(
                log_user=user, log_year=log_year, log_month=log_month, log_day=log_day, log_date=log_date, log_in_time=log_in_time, log_out_time=log_out_time, log_state=log_state)
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

            time_interval = get_time_delta(log_out_time, log_entry.log_in_time)

            log_entry.log_out_time = log_out_time
            log_entry.log_state = 1
            log_entry.interval_time = time_interval
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


class UserTimeRecordSerializer(serializers.Serializer):
    user = serializers.CharField()
    year = serializers.IntegerField()
    month = serializers.IntegerField()
    day = serializers.IntegerField()
    date = serializers.DateField()
    week_day = serializers.CharField()
    log_entries = TimeLogEntrySerializer(many=True)
    mandatory_work_time = serializers.IntegerField()
    mandatory_break_time = serializers.IntegerField()
    total_work_time_for_day = serializers.IntegerField()


class TeamSerializer(serializers.Serializer):
    id = serializers.CharField()
    department = serializers.CharField()
    manager = serializers.CharField(required=False)
    time_log_correction_approver = serializers.CharField(required=False)

    def create(self, validated_data):
        id = validated_data["id"]
        department = validated_data["department"]
        manager = validated_data.get("manager", None)
        time_log_correction_approver = validated_data.get(
            "time_log_correction_approver", None)
        dept_obj = Department.objects.get(pk=department)
        team = Team.objects.create(
            id=id, department=dept_obj, manager=manager, time_log_correction_approver=time_log_correction_approver)

        team.save()


class DepartmentSerializer(serializers.Serializer):
    id = serializers.CharField()
    incharge = serializers.CharField(required=False)

    def create(self, validated_data):
        id = validated_data["id"]
        incharge = validated_data.get("manager", None)
        dept = Department.objects.create(id=id, incharge=incharge)

        dept.save()


class TimeLogCorrectionRequestSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    requester = serializers.CharField()
    approver = serializers.CharField(required=False)
    entry_id = serializers.IntegerField()
    entry_date = serializers.DateField()
    entry_in_time = serializers.TimeField()
    entry_out_time = serializers.TimeField()
    approver_decision = serializers.IntegerField()
    request_date = serializers.DateField()
    request_year = serializers.IntegerField()
    request_month = serializers.IntegerField()
    remark = serializers.CharField()
    decision_date = serializers.DateField(required=False)

    def _check_correction_request_validity(self, requester, entry_date, entry_id, entry_in_time, entry_out_time):
        time_logs = TimeLogEntry.objects.filter(
            log_user=requester, log_date=entry_date)

        total_entries = time_logs.count()
        for i in range(0, total_entries):
            if time_logs[i].id != entry_id:
                continue
            hit_index = i
            break

        if total_entries == 1:
            predecessor = None
            successor = None
        elif total_entries == 0:
            raise AssertionError("This situation should never occur")
        elif total_entries > 1:
            if hit_index == 0:
                predecessor = None
                successor = time_logs[hit_index + 1]
            elif hit_index == total_entries - 1:
                predecessor = time_logs[hit_index - 1]
                successor = None
            else:
                predecessor = time_logs[hit_index - 1]
                successor = time_logs[hit_index + 1]
        else:
            raise AssertionError("This situation should never occur")

        (login_time_bounds, logout_time_bounds) = get_time_entry_bounds_for_correction(
            predecessor, entry_in_time, entry_out_time, successor)
        in_time_in_bound = is_time_within_bounds(
            login_time_bounds[0], entry_in_time, login_time_bounds[1])
        out_time_in_bound = is_time_within_bounds(
            logout_time_bounds[0], entry_out_time, logout_time_bounds[1])

        if (in_time_in_bound and out_time_in_bound):
            return True
        return False

    def create(self, validated_data):
        requester = validated_data['requester']
        approver = validated_data.get('approver', None)
        entry_id = validated_data['entry_id']
        entry_date = validated_data['entry_date']
        entry_in_time = validated_data['entry_in_time']
        entry_out_time = validated_data['entry_out_time']
        approver_decision = validated_data.get('approver_decision', -1)
        request_date = validated_data['request_date']
        request_year = validated_data['request_year']
        request_month = validated_data['request_month']
        remark = validated_data['request_month']
        decision_date = validated_data.get('decision_date', None)

        req_obj = User.objects.get(pk=requester)
        approv_obj = req_obj.team.time_log_correction_approver
        is_valid = self._check_correction_request_validity(
            requester, entry_date, entry_id, entry_in_time, entry_out_time)
        if is_valid:
            correction_obj = TimeLogCorrectionRequest.objects.create(
                requester=req_obj, approver=approv_obj, entry_id=entry_id, entry_date=entry_date, entry_in_time=entry_in_time, entry_out_time=entry_out_time, approver_decision=approver_decision, request_date=request_date, request_year=request_year, request_month=request_month, remark=remark, decision_date=decision_date)

            return (True, correction_obj)
        return (False, None)

    def update(self, instance, validated_data):
        instance.approver_decision = validated_data['approver_decision']
        instance.decision_date = validated_data['decision_date']

        instance.save()

        return instance

# vacation manager


class HolidaySerializer(serializers.Serializer):
    year = serializers.IntegerField()
    month = serializers.IntegerField()
    day = serializers.IntegerField()
    date = serializers.DateField()
    holiday_type = serializers.IntegerField()
    description = serializers.CharField()

    def create(self, validated_data):
        year = validated_data["year"]
        month = validated_data["month"]
        day = validated_data["day"]
        date = validated_data["date"]
        holiday_type = validated_data["holiday_type"]
        description = validated_data.get("description", None)
        status = validated_data.get("status", 0)

        holiday = Holiday.objects.create(
            year=year, month=month, day=day, date=date, holiday_type=holiday_type, description=description, status=status)

        holiday.save()


class VacationSerializer(serializers.Serializer):
    vacation_id = serializers.CharField()
    user = serializers.CharField()
    team = serializers.CharField()
    year = serializers.IntegerField()
    month = serializers.IntegerField()
    day = serializers.IntegerField()
    date = serializers.DateField()
    vacation_type = serializers.CharField()
    action = serializers.IntegerField()
    decision = serializers.IntegerField()
    approver = serializers.CharField()

    def create(self, validated_data):
        vacation_id = validated_data["vacation_id"]
        user = validated_data["user"]
        team = validated_data["team"]
        year = validated_data["year"]
        month = validated_data["month"]
        day = validated_data["day"]
        date = validated_data["date"]
        vacation_type = validated_data["vacation_type"]
        action = validated_data["action"]
        status = validated_data.get("status", 0)
        decision = validated_data["decision"]
        approver = validated_data["approver"]

        user_obj = User.objects.get(pk=user)
        vacation = Vacation.objects.create(
            vacation_id=vacation_id, user=user_obj, team=team, year=year, month=month, day=day, date=date, vacation_type=vacation_type, action=action, status=status,
            decision=decision, approver=approver)

        vacation.save()


class ConflictGroupSerializer(serializers.Serializer):
    id = serializers.CharField()
    team = serializers.CharField()
    status = serializers.IntegerField()

    def create(self, validated_data):
        id = validated_data["id"]
        team = validated_data["team"]
        status = validated_data["status"]
        # team_obj = Team.objects.get(pk=team)
        cg = ConflictGroup.objects.create(
            id=id, team=team, status=status)

        cg.members.set([])
        cg.save()
