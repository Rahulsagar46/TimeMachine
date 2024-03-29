from django.urls import path
from timelog.views import log_time_entry
from timelog.views import load_initial_values
from timelog.views import add_new_user
from timelog.views import add_new_team
from timelog.views import add_new_department
from timelog.views import get_log_entries
from timelog.views import edit_log_entry
from timelog.views import get_open_correction_requests
from timelog.views import decide_correction_entry
from timelog.views import add_holiday_list
from timelog.views import add_vacation
from timelog.views import get_team_vacation_info
from timelog.views import add_conflict_group_for_team

urlpatterns = [
    # GET requests
    path('<str:user_login>', load_initial_values),
    path('getlog/<str:user_login>/<str:date>', get_log_entries),
    path('getcorrectionrequests/<str:approver_name>',
         get_open_correction_requests),
    path('teamcalendar/<str:main_user>', get_team_vacation_info),
    # POST requests
    path('add/', add_new_user),
    path('newteam/', add_new_team),
    path('newdepartment/', add_new_department),
    path('punch/', log_time_entry),
    path('editlog/', edit_log_entry),
    path('decide/', decide_correction_entry),
    path('addholidays/', add_holiday_list),
    path('addvacation/', add_vacation),
    path('addcg/', add_conflict_group_for_team)
]
