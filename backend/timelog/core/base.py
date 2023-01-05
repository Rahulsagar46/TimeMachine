from datetime import datetime


def convert_time_str_to_time_obj(time_str, format="%H:%M:%S"):
    assert isinstance(
        time_str, str), "Invalid value passed to the parameter 'time_str'"

    time_obj = datetime.strptime(time_str, format).time()

    return time_obj


def get_time_delta(time_a, time_b):
    # assert isinstance(time_a, datetime.time), "Invalid value passed"
    # assert isinstance(time_b, datetime.time), "Invalid value passed"

    total_seconds_a = (time_a.hour * 60 * 60) + \
        (time_a.minute * 60) + time_a.second
    total_seconds_b = (time_b.hour * 60 * 60) + \
        (time_b.minute * 60) + time_b.second

    total_diff_in_sec = total_seconds_a - total_seconds_b

    return total_diff_in_sec
