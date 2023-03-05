from datetime import datetime, date
from django.db import models
from django.db.models.functions import Coalesce

# custom model managers


class UserCustomManager1(models.Manager):
    def get(self, login_name=None):
        # This method returns the contents of User, UserDefault, UserTimeSummary tables for a specific user
        user_details = User.objects.filter(login_name=login_name)
        if user_details.count() == 0:
            # Incase of unknown user
            raise User.DoesNotExist
        user_obj = user_details[0]
        user_defaults = user_obj.userdefault
        user_summary = user_obj.usertimesummary
        user_live_status = user_obj.userlivestatus

        q_obj = user_details.annotate(
            mandatory_break_time=Coalesce(user_defaults.mandatory_break_time, 0))
        q_obj = q_obj.annotate(
            mandatory_working_time_per_day=Coalesce(user_defaults.mandatory_working_time_per_day, 0))
        q_obj = q_obj.annotate(net_working_time=Coalesce(
            user_summary.net_working_time, 0))
        q_obj = q_obj.annotate(last_update=Coalesce(
            user_live_status.last_update, datetime.now()))
        q_obj = q_obj.annotate(live_state=Coalesce(
            user_live_status.live_state, 0))

        return q_obj.get()

    def create(self, login_name, sap_id, first_name, last_name, email_id, status, mandatory_break_time, mandatory_working_time_per_day, net_working_time, department_obj, team_obj):
        # add user
        new_user = User.objects.create(
            login_name=login_name, sap_id=sap_id, first_name=first_name, last_name=last_name, email_id=email_id, status=status, department=department_obj, team=team_obj)

        new_user.save()

        # add user defaults
        new_user_defaults = UserDefault.objects.create(
            user=new_user, mandatory_break_time=mandatory_break_time, mandatory_working_time_per_day=mandatory_working_time_per_day)

        # add user summary fields
        new_user_time_summary = UserTimeSummary.objects.create(
            user=new_user, net_working_time=net_working_time)

        # add user live status fields
        user_live_status = UserLiveStatus.objects.create(
            user=new_user, last_update=datetime.now(), live_state=0)

        new_user_defaults.save()
        new_user_time_summary.save()
        user_live_status.save()

        return new_user

# models


class User(models.Model):
    # Default model manager
    objects = models.Manager()
    # custom model manager used for initial loading
    objects_include_related = UserCustomManager1()

    login_name = models.CharField(
        max_length=100, primary_key=True, unique=True)
    sap_id = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_id = models.EmailField(max_length=100)
    status = models.IntegerField(
        choices=[(0, "inactive"), (1, "active")], default=1)
    department = models.ForeignKey(
        'Department', on_delete=models.PROTECT, null=True)
    team = models.ForeignKey(
        'Team', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.login_name


class UserDefault(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    # normally 30 minutes per day == 1800 seconds
    mandatory_break_time = models.IntegerField()
    # normally 8hours == 28800 seconds
    mandatory_working_time_per_day = models.IntegerField()

    def __str__(self):
        return "%s_defaults" % (self.user, )


class UserTimeSummary(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    net_working_time = models.IntegerField()

    def __str__(self):
        return "%s_summary" % (self.user, )


class TimeLogEntry(models.Model):
    log_user = models.ForeignKey('User', on_delete=models.CASCADE)
    log_year = models.IntegerField()
    log_month = models.IntegerField()
    log_day = models.IntegerField()
    log_date = models.DateField()
    log_in_time = models.TimeField()
    log_out_time = models.TimeField(null=True)
    log_state = models.IntegerField(
        choices=[(0, "unsettled"), (1, "settled"), (2, "approval pending")])
    interval_time = models.IntegerField(default=0)

    def __str__(self):
        return "%s_%s_%s" % (self.log_date, self.log_user, self.log_state)


class UserLiveStatus(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    last_update = models.DateTimeField()
    live_state = models.IntegerField(choices=[(0, "out"), (1, "in")])
    active_log = models.IntegerField(default=-1)

    def __str__(self):
        return "%s_livestatus" % (self.user, )


class UserTimeRecord(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()
    date = models.DateField()
    week_day = models.CharField(max_length=15)
    log_entries = models.ManyToManyField('TimeLogEntry', default=[])
    mandatory_work_time = models.IntegerField()
    mandatory_break_time = models.IntegerField()
    total_work_time_for_day = models.IntegerField()

    def __str__(self):
        return "%s_%s" % (self.date, self.user)


class Department(models.Model):
    id = models.CharField(max_length=50, primary_key=True, unique=True)
    # teams = models.ManyToManyField('Team', default=[])
    # This on_delete parameter is wrong. When the user is deleted, the department must not be deleted
    incharge = models.ForeignKey(
        'User', on_delete=models.PROTECT, related_name='hod', null=True)

    def __str__(self):
        return self.id


class Team(models.Model):
    id = models.CharField(max_length=50, primary_key=True, unique=True)
    department = models.ForeignKey(
        'Department', on_delete=models.PROTECT, related_name='subteam', null=True)
    manager = models.ForeignKey(
        'User', on_delete=models.PROTECT, related_name='incharge', null=True)
    time_log_correction_approver = models.ForeignKey(
        'User', on_delete=models.PROTECT, related_name='time_log_approver', null=True)

    def __str__(self):
        return self.id


class TimeLogCorrectionRequest(models.Model):
    requester = models.ForeignKey(
        'User', on_delete=models.CASCADE, related_name='requested_by')
    approver = models.ForeignKey(
        'User', on_delete=models.PROTECT, related_name='tba_by')
    entry_id = models.IntegerField()
    entry_date = models.DateField()
    entry_in_time = models.TimeField()
    entry_out_time = models.TimeField()
    approver_decision = models.IntegerField(
        choices=[(-1, 'decision pending'), (0, 'rejected'), (1, 'approved')])
    request_date = models.DateField()
    decision_date = models.DateField(null=True)

    def __str__(self):
        return "%s_%s_%s_%s" % (self.request_date, self.requester, self.approver, self.approver_decision)
