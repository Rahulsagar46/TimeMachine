from django.db import models


class User(models.Model):
    unique_id = models.CharField(max_length=10, primary_key=True, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_id = models.CharField(max_length=100)
    login_name = models.CharField(max_length=100)

    def __str__(self):
        return "%s %s_%s" % (self.first_name, self.last_name, self.unique_id)


class UserDefaults(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    # normally 30 minutes per day == 1800 seconds
    mandatory_break_time = models.IntegerField()
    # normally 8hours == 28800 seconds
    mandatory_working_time_per_day = models.IntegerField()
