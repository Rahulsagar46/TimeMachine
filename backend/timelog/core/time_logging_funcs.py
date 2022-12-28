import time


def record_work_in_time():
    work_in_time = time.time()
    default_user = "rvoduru"

    return "%s logged in at %s" % (default_user, work_in_time,)
