from django.contrib import admin
from timelog.models import User, UserDefault, UserTimeSummary


admin.site.register(User)
admin.site.register(UserDefault)
admin.site.register(UserTimeSummary)
