import requests
import json
from datetime import date, datetime

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

datetime_now = datetime.now()
log_date = datetime_now.strftime("%Y-%m-%d")
log_time = datetime_now.strftime("%H:%M:%S")


def add_time_log_entry():
    time_log_entry = {
        "log_user": "rvoduru",
        "log_date": log_date,
        "log_in_time": log_time,
        "log_out_time": log_time,
        "log_state": 0
    }
    r = requests.post("http://127.0.0.1:8000/punch/",
                      json=time_log_entry, headers=headers)

    print(r.json)


def add_test_users():
    # user_data1 = {
    #     "login_name": "rahulv",
    #     "sap_id": "700101",
    #     "first_name": "Manager",
    #     "last_name": "Y",
    #     "email_id": "xyz@gmail.com",
    #     "department": "D1",
    #     "team": "T1",
    #     "mandatory_break_time": 2400,
    #     "mandatory_working_time_per_day": 28800,
    #     "net_working_time": 21600
    # }

    # user_data2 = {
    #     "login_name": "manager1",
    #     "sap_id": "700102",
    #     "first_name": "Manager",
    #     "last_name": "Y",
    #     "email_id": "xyz@gmail.com",
    #     "department": "D1",
    #     "team": "T1",
    #     "mandatory_break_time": 2400,
    #     "mandatory_working_time_per_day": 28800,
    #     "net_working_time": 21600
    # }

    user_data3 = {
        "login_name": "user2",
        "sap_id": "700103",
        "first_name": "User2",
        "last_name": "XY",
        "email_id": "xyz@gmail.com",
        "department": "D1",
        "team": "T1",
        "mandatory_break_time": 2400,
        "mandatory_working_time_per_day": 28800,
        "net_working_time": 21600
    }

    user_data4 = {
        "login_name": "user3",
        "sap_id": "700104",
        "first_name": "User3",
        "last_name": "ZL",
        "email_id": "xyz@gmail.com",
        "department": "D1",
        "team": "T1",
        "mandatory_break_time": 2400,
        "mandatory_working_time_per_day": 28800,
        "net_working_time": 21600
    }

    r = requests.post("http://127.0.0.1:8000/add/",
                      json=user_data4, headers=headers)
    print(r.json)


def add_new_dept():
    dept_info = {
        "id": "D1",
    }
    r = requests.post("http://127.0.0.1:8000/newdepartment/",
                      json=dept_info, headers=headers)
    print(r.json)


def add_new_team():
    team_info = {
        "id": "T1",
        "department": "D1"
    }
    r = requests.post("http://127.0.0.1:8000/newteam/",
                      json=team_info, headers=headers)
    print(r.json)


def edit_time_log():
    time_log_corrected = {
        "requester": "rvoduru",
        "entry_id": 2,
        "entry_date": "2023-03-11",
        "entry_in_time": "15:30:45",
        "entry_out_time": "15:37:51",
        "approver_decision": -1,
        "request_date": "2023-03-11",
        "request_year": 2023,
        "request_month": 3,
        "remark": "hello test test"
    }
    r = requests.post("http://127.0.0.1:8000/editlog/",
                      json=time_log_corrected, headers=headers)

    print(r.json)


def decide_correction():
    decision_dict = {
        "approver": "mwendl",
        "id": 6,
        "entry_id": 4,
        "approver_decision": 1,
        "decision_date": "2023-01-12"
    }
    r = requests.post("http://127.0.0.1:8000/decide/",
                      json=decision_dict, headers=headers)

    print(r.json)


def add_holidays():
    holiday_list = [
        {
            "date": "2023-04-07",
            "holiday_type": 0,
            "description": "Good Friday"
        },
        {
            "date": "2023-04-10",
            "holiday_type": 0,
            "description": "Easter Monday"
        },
        {
            "date": "2023-05-01",
            "holiday_type": 0,
            "description": "Labour day"
        },
        {
            "date": "2023-05-18",
            "holiday_type": 0,
            "description": "Ascension day"
        },
        {
            "date": "2023-05-29",
            "holiday_type": 0,
            "description": "Whit Monday"
        },
        {
            "date": "2023-06-08",
            "holiday_type": 0,
            "description": "Corpus Christi"
        },
        {
            "date": "2023-08-15",
            "holiday_type": 0,
            "description": "Assumption Day"
        },
        {
            "date": "2023-10-03",
            "holiday_type": 0,
            "description": "Day of German Unity"
        },
        {
            "date": "2023-11-01",
            "holiday_type": 0,
            "description": "All Saints days"
        },
        {
            "date": "2023-12-25",
            "holiday_type": 0,
            "description": "Christmas day"
        },
        {
            "date": "2023-12-26",
            "holiday_type": 0,
            "description": "2nd day of Christmas"
        }
    ]

    send_dict = {
        "holiday_list": holiday_list
    }
    r = requests.post("http://127.0.0.1:8000/addholidays/",
                      json=send_dict, headers=headers)
    print(r.json)


def add_vacation():
    vacation_dict = {
        "common": {
            "user": "rahulv",
            "vacation_type": "Urlaub",
            "action": 0,
            "decision": -1,
            "approver": "manager1",
            "team": "T1"
        },
        "actual": ["2023-04-05", "2023-04-06"]
    }

    r = requests.post("http://127.0.0.1:8000/addvacation/",
                      json=vacation_dict, headers=headers)
    print(r.json)


def add_conflict_group():
    send_dict = {
        "id": "Group-1",
        "team": "T1",
        # "members": ["rahulv", "user2", "user3"],
        "status": 0
    }
    r = requests.post("http://127.0.0.1:8000/addcg/",
                      json=send_dict, headers=headers)
    print(r.json)


if __name__ == "__main__":
    # edit_time_log()
    # add_time_log_entry()
    # add_new_dept()
    # add_new_team()
    # add_test_users()
    # decide_correction()
    # add_holidays()
    # add_vacation()
    # add_conflict_group()
    pass
