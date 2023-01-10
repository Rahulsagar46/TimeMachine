from timelog.models import TimeLogEntry, TimeLogCorrectionRequest
from timelog.serializers import TimeLogEntrySerializer, TimeLogCorrectionRequestSerializer


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
    if is_valid:
        updated_instance = serializer.update(
            correction_req_instance, update)
        return (True, updated_instance)
    return (False, serializer.errors)
