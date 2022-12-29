from django.contrib import admin
from timelog.models import User, UserDefaults


admin.site.register(User)
admin.site.register(UserDefaults)
