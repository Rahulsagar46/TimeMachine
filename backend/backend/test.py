import requests
import json

in_dict = {
    "login_name": "cjuergen",
    "sap_id": "700103",
    "first_name": "Christoph",
    "last_name": "Juergen",
    "email_id": "cjcjcjc@gmail.com",
    "mandatory_break_time": 1800,
    "mandatory_working_time_per_day": 28800,
    "net_working_hrs": 21600
}

json_data = json.dumps(in_dict)
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}
# r = requests.post("http://127.0.0.1:8000/add/", json=in_dict, headers=headers)
# print(r.json)
