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


def get_time_entry_bounds_for_correction(predecesssor, current_log_in, current_log_out, successor):
    login_left_limit = None if predecesssor == None else predecesssor.log_out_time
    login_right_limit = None if current_log_out == None else current_log_out
    logout_left_limit = current_log_in
    logout_right_limit = None if successor == None else successor.log_in_time

    return ((login_left_limit, login_right_limit), (logout_left_limit, logout_right_limit))
