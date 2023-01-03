from timelog.serializers import TimeLogEntrySerializer


def record_time_entry(time_log_entry):
    serializer = TimeLogEntrySerializer(data=time_log_entry)
    is_valid = serializer.is_valid()
    if is_valid:
        ack = serializer.create(serializer.data)
        return (True, ack)
    else:
        return (False, serializer.errors)
