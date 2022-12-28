
from django.shortcuts import render
from django.http import HttpResponse
from timelog.core.time_logging_funcs import record_work_in_time

# time entry functions


def log_time_entry(request):
    response = record_work_in_time()
    return HttpResponse(response)

# user management function


def add_new_user(request):
    return HttpResponse()

# read functions


def get_time_summary_for_user(request):
    return HttpResponse()
