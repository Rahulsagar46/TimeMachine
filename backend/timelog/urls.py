from django.urls import path
from timelog.views import log_time_entry, get_list_of_users, load_initial_values

urlpatterns = [
    path('punch/', log_time_entry),
    path('<str:user_login>', load_initial_values)
]
