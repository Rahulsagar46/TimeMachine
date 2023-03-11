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
    user_data = {
        "login_name": "philm",
        "sap_id": "700102",
        "first_name": "XXX",
        "last_name": "Y",
        "email_id": "xyz@gmail.com",
        "department": "PD",
        "team": "PSG",
        "mandatory_break_time": 2400,
        "mandatory_working_time_per_day": 28800,
        "net_working_time": 21600
    }
    r = requests.post("http://127.0.0.1:8000/add/",
                      json=user_data, headers=headers)
    print(r.json)


def add_new_dept():
    dept_info = {
        "id": "PD",
    }
    r = requests.post("http://127.0.0.1:8000/newdepartment/",
                      json=dept_info, headers=headers)
    print(r.json)


def add_new_team():
    team_info = {
        "id": "PSG",
        "department": "PD"
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


if __name__ == "__main__":
    # edit_time_log()
    # add_time_log_entry()
    # add_new_dept()
    # add_new_team()
    # add_test_users()
    # decide_correction()
    pass
