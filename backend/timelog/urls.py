from django.urls import path
from timelog.views import log_time_entry, load_initial_values, add_new_user

urlpatterns = [
    path('punch/', log_time_entry),
    path('<str:user_login>', load_initial_values),
    path('add/', add_new_user)
]
