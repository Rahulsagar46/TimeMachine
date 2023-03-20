import time
import datetime
from timelog.models import User
from timelog.models import Holiday
from timelog.models import Vacation
from timelog.models import ConflictGroup
from timelog.serializers import UserSerializer
from timelog.serializers import HolidaySerializer
from timelog.serializers import VacationSerializer
from timelog.serializers import ConflictGroupSerializer


def get_team_calendar_info(main_user):
    usr_obj = User.objects.get(pk=main_user)
    team = usr_obj.team
    holiday_list = Holiday.objects.filter(year=2023, status=0)
    holiday_serializer = HolidaySerializer(holiday_list, many=True)

    vacation_list = Vacation.objects.filter(year=2023, status=0, team=team)
    vacation_serializer = VacationSerializer(vacation_list, many=True)
    planned_vacations = []
    applied_vacations = []
    for holiday in vacation_serializer.data:
        if holiday["action"] == 0:
            planned_vacations.append(holiday)
        elif holiday["action"] == 1:
            applied_vacations.append(holiday)
        else:
            raise AssertionError("invalid holiday action %s" %
                                 (holiday["action"]))
    return_obj = {
        "common": {
            "user": main_user,
            "team": team.id,
            "approver": team.manager.login_name
        },
        "holidays": holiday_serializer.data,
        "planned": planned_vacations,
        "applied": applied_vacations
    }

    return return_obj


def add_holiday_entries(holiday_dict):
    holiday_list = holiday_dict["holiday_list"]
    for holiday in holiday_list:
        date_obj = datetime.datetime.strptime(holiday["date"], "%Y-%m-%d")
        holiday["day"] = date_obj.day
        holiday["month"] = date_obj.month - 1
        assert 0 <= holiday["month"] <= 11, "Invalid month index"
        holiday["year"] = date_obj.year
    serializer = HolidaySerializer(data=holiday_list, many=True)
    is_valid = serializer.is_valid()
    if is_valid:
        holiday_entries = serializer.create(serializer.data)
        return (True, holiday_entries)
    else:
        return (False, serializer.errors)


def add_vacation_entries(vacation_dict):
    common = vacation_dict["common"]
    common["vacation_id"] = "%s_%s" % (common["user"], time.time())
    vacations_actual = vacation_dict["actual"]
    final_vacation_list = []
    for vacation in vacations_actual:
        day_dict = {}
        for key in common.keys():
            day_dict[key] = common[key]
        day_dict["date"] = vacation
        date_obj = datetime.datetime.strptime(vacation, "%Y-%m-%d")
        day_dict["day"] = date_obj.day
        day_dict["month"] = date_obj.month - 1
        assert 0 <= day_dict["month"] <= 11, "Invalid month index"
        day_dict["year"] = date_obj.year
        final_vacation_list.append(day_dict)
    serializer = VacationSerializer(data=final_vacation_list, many=True)
    is_valid = serializer.is_valid()
    if is_valid:
        vacation_entries = serializer.create(serializer.data)
        return (True, vacation_entries)
    else:
        print(serializer.errors)
        return (False, serializer.errors)


def add_conflict_group(cg_dict):
    # usr_obj_list = []
    # for member in cg_dict["members"]:
    #     usr_obj = User.objects.get(pk=member)
    #     usr_obj_list.append(usr_obj)
    # user_serializer = UserSerializer(usr_obj_list, many=True)
    # cg_dict["members"] = user_serializer.data
    cg_serializer = ConflictGroupSerializer(data=cg_dict)
    is_valid = cg_serializer.is_valid()
    if is_valid:
        cg_dict_return = cg_serializer.create(cg_serializer.data)
        return (True, cg_dict_return)
    else:
        print(cg_serializer.errors)
        return (False, cg_serializer.errors)
