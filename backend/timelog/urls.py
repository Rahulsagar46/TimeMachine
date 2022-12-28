from django.urls import path
from timelog.views import log_time_entry

urlpatterns = [
    path('punch/', log_time_entry),
    path('', log_time_entry)
]
