
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from timelog.core.time_logging_funcs import record_time_entry, get_all_time_entries, request_log_entry_correction, get_all_open_correction_requests, decide_log_entry_correction
from timelog.core.time_logging_funcs import get_all_time_entries_for_the_month
from timelog.core.time_logging_funcs import get_relevant_correction_requests
from timelog.core.user_management_funcs import list_all_users, get_initial_user_details, create_new_user_with_relevant_data
from timelog.core.team_management_funcs import create_new_team, create_new_department
from timelog.core.vacation_management_funcs import add_holiday_entries, add_vacation_entries, get_team_calendar_info, add_conflict_group

# initial loading parameters


@api_view(['GET'])
def load_initial_values(request, user_login):
    (success, user_details) = get_initial_user_details(user_login)
    log_entries = get_all_time_entries_for_the_month(user_login)
    user_details["log_entries"] = log_entries
    correction_requests = get_relevant_correction_requests(user_login)
    user_details["correction_requests"] = correction_requests
    if success:
        return Response(user_details)
    return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_log_entries(request, user_login, date):
    log_entries = get_all_time_entries(user_login, date)
    return JsonResponse(log_entries, safe=False)


@api_view(['GET'])
def get_open_correction_requests(request, approver_name):
    correction_requests = get_all_open_correction_requests(approver_name)
    return JsonResponse(correction_requests, safe=False)


@api_view(['GET'])
def get_relevant_correction_requests_for_requester(request, requester):
    correction_requests = get_relevant_correction_requests(requester)
    return JsonResponse(correction_requests, safe=False)

# vacation management get


@api_view(['GET'])
def get_team_vacation_info(request, main_user):
    return_obj = get_team_calendar_info(main_user)
    return JsonResponse(return_obj, safe=False)

# time entry functions


@api_view(['POST'])
@csrf_exempt  # NOTE: This has to be removed in production. This is a safety mechanism
def log_time_entry(request):
    (success, return_data) = record_time_entry(request.data)
    if success:
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# user management function


@api_view(['POST'])
@csrf_exempt  # NOTE: This has to be removed in production. This is a safety mechanism
def add_new_user(request):
    (success, return_data) = create_new_user_with_relevant_data(request.data)
    if success:
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


def get_list_of_users(request):
    user_list_json = list_all_users()
    return JsonResponse(user_list_json, safe=False)


@api_view(['POST'])
@csrf_exempt  # NOTE: This has to be removed in production. This is a safety mechanism
def add_new_team(request):
    (success, return_data) = create_new_team(request.data)
    if success:
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@csrf_exempt  # NOTE: This has to be removed in production. This is a safety mechanism
def add_new_department(request):
    (success, return_data) = create_new_department(request.data)
    if success:
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@csrf_exempt  # NOTE: This has to be removed in production. This is a safety mechanism
def edit_log_entry(request):
    (success, return_data) = request_log_entry_correction(request.data)
    if success:
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@csrf_exempt  # NOTE: This has to be removed in production. This is a safety mechanism
def decide_correction_entry(request):
    (success, return_data) = decide_log_entry_correction(request.data)
    if success:
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# vacation management views


@api_view(['POST'])
@csrf_exempt  # NOTE: This has to be removed in production. This is a safety mechanism
def add_holiday_list(request):
    (success, return_data) = add_holiday_entries(request.data)
    if success:
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@csrf_exempt  # NOTE: This has to be removed in production. This is a safety mechanism
def add_vacation(request):
    (success, return_data) = add_vacation_entries(request.data)
    if success:
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@csrf_exempt  # NOTE: This has to be removed in production. This is a safety mechanism
def add_conflict_group_for_team(request):
    (success, return_data) = add_conflict_group(request.data)
    if success:
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)
