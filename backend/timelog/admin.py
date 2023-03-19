from django.contrib import admin
from timelog.models import User, UserDefault, UserTimeSummary, TimeLogEntry, UserLiveStatus, UserTimeRecord
from timelog.models import Department, Team, TimeLogCorrectionRequest, Holiday, Vacation, ConflictGroup


admin.site.register(User)
admin.site.register(UserDefault)
admin.site.register(UserTimeSummary)
admin.site.register(TimeLogEntry)
admin.site.register(UserLiveStatus)
admin.site.register(UserTimeRecord)
admin.site.register(Department)
admin.site.register(Team)
admin.site.register(TimeLogCorrectionRequest)
admin.site.register(Holiday)
admin.site.register(Vacation)
admin.site.register(ConflictGroup)
