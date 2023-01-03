import requests
import json

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}


def add_time_log_entry():
    time_log_entry = {
        "log_user": "rvoduru",
        "log_date": "2023-01-03",
        "log_time": "12:30:23",
        "log_type": 0
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
        "net_working_hrs": 21600
    }
    r = requests.post("http://127.0.0.1:8000/add/",
                      json=user_data, headers=headers)
    print(r.json)


if __name__ == "__main__":
    # add_time_log_entry()
    # add_test_users()
    pass
