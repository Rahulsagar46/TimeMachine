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
        "log_user": "jpduggineni",
        "log_date": log_date,
        "log_in_time": log_time,
        # "log_out_time": log_time,
        "log_state": 0
    }
    r = requests.post("http://127.0.0.1:8000/punch/",
                      json=time_log_entry, headers=headers)

    print(r.json)


def add_test_users():
    user_data = {
        "login_name": "jpduggineni",
        "sap_id": "700101",
        "first_name": "Jayaprakash",
        "last_name": "Duggineni",
        "email_id": "jpd@gmail.com",
        "mandatory_break_time": 1800,
        "mandatory_working_time_per_day": 28800,
        "net_working_time": 21600
    }
    r = requests.post("http://127.0.0.1:8000/add/",
                      json=user_data, headers=headers)
    print(r.json)


if __name__ == "__main__":
    # add_time_log_entry()
    # add_test_users()
    pass
