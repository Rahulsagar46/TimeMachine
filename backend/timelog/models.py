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
