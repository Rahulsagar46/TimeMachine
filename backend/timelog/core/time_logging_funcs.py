from timelog.models import TimeLogEntry
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
        ack = serializer.create(serializer.data)
        return (True, ack)
    else:
        return (False, serializer.errors)
