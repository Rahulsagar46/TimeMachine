
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from timelog.core.time_logging_funcs import record_work_in_time
from timelog.core.user_management_funcs import list_all_users, get_initial_user_details

# initial loading parameters


@api_view(['GET'])
def load_initial_values(request, user_login):
    (success, user_details) = get_initial_user_details(user_login)
    if success:
        return Response(user_details)
    return Response(status=status.HTTP_404_NOT_FOUND)


# time entry functions


def log_time_entry(request):
    response = record_work_in_time()
    return HttpResponse(response)

# user management function


def add_new_user(request):
    return HttpResponse()


def get_list_of_users(request):
    user_list_json = list_all_users()
    return JsonResponse(user_list_json, safe=False)
