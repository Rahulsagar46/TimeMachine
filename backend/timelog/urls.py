from django.urls import path
from timelog.views import log_time_entry, load_initial_values, add_new_user, add_new_team, get_log_entries, edit_log_entry

urlpatterns = [
    path('punch/', log_time_entry),
    path('<str:user_login>', load_initial_values),
    path('add/', add_new_user),
    path('newteam/', add_new_team),
    path('getlog/<str:user_login>/<str:date>', get_log_entries),
    path('editlog/', edit_log_entry)
]
