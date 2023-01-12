from timelog.models import TimeLogEntry, TimeLogCorrectionRequest, UserTimeRecord
from timelog.serializers import TimeLogEntrySerializer, TimeLogCorrectionRequestSerializer

from timelog.core.base import get_time_delta


def record_time_entry(time_log_entry):
    serializer = TimeLogEntrySerializer(data=time_log_entry)
    is_valid = serializer.is_valid()
    if is_valid:
        ack = serializer.create(serializer.data)
        return (True, ack)
    else:
        return (False, serializer.errors)


def get_all_time_entries(user, date):
    log_entries = TimeLogEntry.objects.filter(log_user=user, log_date=date)
    serializer = TimeLogEntrySerializer(log_entries, many=True)

    return serializer.data


def request_log_entry_correction(corrected_log_entry):
    serializer = TimeLogCorrectionRequestSerializer(data=corrected_log_entry)
    is_valid = serializer.is_valid()
    if is_valid:
        (status, return_obj) = serializer.create(serializer.data)
        if status:
            log_entry_id = corrected_log_entry["entry_id"]
            time_log_entry_object = TimeLogEntry.objects.get(pk=log_entry_id)
            time_log_entry_object.log_state = 2  # change state to approval pending
            time_log_entry_object.save()
        return (status, return_obj)
    else:
        return (False, serializer.errors)


def get_all_open_correction_requests(approver_name):
    correction_requests = TimeLogCorrectionRequest.objects.filter(
        approver=approver_name, approver_decision=-1)
    serializer = TimeLogCorrectionRequestSerializer(
        correction_requests, many=True)
    return serializer.data


def decide_log_entry_correction(input_dict):
    assert "approver" in input_dict, "error"
    assert "id" in input_dict, "error"
    assert "entry_id" in input_dict, "error"
    assert "approver_decision" in input_dict, "error"
    approver = input_dict["approver"]
    correction_id = input_dict["id"]
    decision = input_dict["approver_decision"]
    decision_date = input_dict["decision_date"]
    entry_id = input_dict["entry_id"]
    assert decision in [0, 1], "Invalid input"

    correction_req_instance = TimeLogCorrectionRequest.objects.filter(
        approver=approver, id=correction_id, approver_decision=-1).get()

    update = {
        "approver_decision": decision,
        "decision_date": decision_date
    }
    serializer = TimeLogCorrectionRequestSerializer(
        correction_req_instance, data=update, partial=True)
    is_valid = serializer.is_valid()
    if not is_valid:
        return (False, serializer.errors)
    updated_instance = serializer.update(
        correction_req_instance, update)
    # update target log_entry with corrected data
    time_log_entry_object = TimeLogEntry.objects.get(pk=entry_id)
    time_log_entry_object.log_in_time = correction_req_instance.entry_in_time
    time_log_entry_object.log_out_time = correction_req_instance.entry_out_time
    time_log_entry_object.interval_time = get_time_delta(
        correction_req_instance.entry_out_time, correction_req_instance.entry_in_time)
    time_log_entry_object.log_state = 1  # change state back to settled
    time_log_entry_object.save()
    # update total working time for the day
    update_total_time(time_log_entry_object.log_user,
                      time_log_entry_object.log_date)
    return (True, updated_instance)


def calculate_total_time_for_day(user_name, date):
    log_entries = get_all_time_entries(user_name, date)
    time_sum = 0
    unsettled_entries_exist = False
    for entry in log_entries:
        if entry["log_state"] != 1:
            unsettled_entries_exist = True
        time_sum = time_sum + entry["interval_time"]

    return (unsettled_entries_exist, time_sum)


def update_total_time(user_name, date):
    (unsettled_entries_exist, time_sum) = calculate_total_time_for_day(user_name, date)
    time_record_object = UserTimeRecord.objects.filter(
        user=user_name, date=date).get()
    time_record_object.total_work_time_for_day = time_sum
    time_record_object.save()
