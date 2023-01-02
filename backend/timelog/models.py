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
        user_defaults = user_obj.userdefault_set.get()
        user_summary = user_obj.usertimesummary_set.get()

        q_obj = user_details.annotate(
            mandatory_break_time=Coalesce(user_defaults.mandatory_break_time, 0))
        q_obj = q_obj.annotate(
            mandatory_working_time_per_day=Coalesce(user_defaults.mandatory_working_time_per_day, 0))
        q_obj = q_obj.annotate(net_working_hrs=Coalesce(
            user_summary.net_working_hrs, 0))

        return q_obj.get()

    def create(self, login_name, sap_id, first_name, last_name, email_id, status, mandatory_break_time, mandatory_working_time_per_day, net_working_hrs):
        # add user
        new_user = User.objects.create(
            login_name=login_name, sap_id=sap_id, first_name=first_name, last_name=last_name, email_id=email_id, status=status)

        new_user.save()

        # add user defaults
        new_user_defaults = UserDefault.objects.create(
            user=new_user, mandatory_break_time=mandatory_break_time, mandatory_working_time_per_day=mandatory_working_time_per_day)

        # add user summary fields
        new_user_time_summary = UserTimeSummary.objects.create(
            user=new_user, net_working_hrs=net_working_hrs)

        new_user_defaults.save()
        new_user_time_summary.save()

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
    email_id = models.CharField(max_length=100)
    status = models.IntegerField(
        choices=[(0, "inactive"), (1, "active")], default=1)

    def __str__(self):
        return self.login_name


class UserDefault(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    # normally 30 minutes per day == 1800 seconds
    mandatory_break_time = models.IntegerField()
    # normally 8hours == 28800 seconds
    mandatory_working_time_per_day = models.IntegerField()

    def __str__(self):
        return "%s_defaults" % (self.user, )


class UserTimeSummary(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    net_working_hrs = models.IntegerField()

    def __str__(self):
        return "%s_summary" % (self.user, )
