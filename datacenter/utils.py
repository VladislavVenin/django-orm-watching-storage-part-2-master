from django.utils.timezone import localtime


def get_duration(visit):
    if visit.leaved_at is None:
        moscow_time = localtime()
        duration = moscow_time - visit.entered_at
        return duration.seconds
    else:
        duration = visit.leaved_at - visit.entered_at
        return duration.seconds


def format_duration(duration):
    hours = duration//3600
    minutes = duration % 3600 // 60
    formated = f"{hours}ч, {minutes}мин"
    return formated


def is_visit_long(visit, minutes=60):
    if visit.leaved_at is not None:
        duration = visit.leaved_at - visit.entered_at
        duration = duration.total_seconds()/60
        if duration > minutes:
            return True
    else:
        duration = get_duration()/60
        if duration > minutes:
            return True
        return False
    return False
