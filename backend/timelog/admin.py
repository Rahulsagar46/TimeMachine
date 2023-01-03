from django.contrib import admin
from timelog.models import User, UserDefault, UserTimeSummary, TimeLogEntry, UserLiveStatus


admin.site.register(User)
admin.site.register(UserDefault)
admin.site.register(UserTimeSummary)
admin.site.register(TimeLogEntry)
admin.site.register(UserLiveStatus)
