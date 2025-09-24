from django.utils.timezone import localtime


def get_duration(visit):
    if visit.leaved_at is None:
        moscow_time = localtime()
        duration = moscow_time - visit.entered_at
    else:
        duration = visit.leaved_at - visit.entered_at
    return duration.total_seconds()


def format_duration(duration):
    hour = 3600
    minute = 60
    hours = duration//hour
    minutes = duration % hour // minute
    formated = f"{hours}ч, {minutes}мин"
    return formated


def is_visit_long(duration, long_visit=60):
    minute = 60
    if duration/minute > long_visit:
        return True
    return False
