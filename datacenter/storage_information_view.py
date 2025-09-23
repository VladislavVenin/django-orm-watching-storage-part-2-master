from datacenter.models import Visit
from django.shortcuts import render
from datacenter.utils import get_duration, format_duration


def storage_information_view(request):
    active_passcards = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []
    for entered in active_passcards:
        duration = get_duration(entered)
        non_closed_visit = {
                'who_entered': entered.passcard,
                'entered_at': entered.entered_at,
                'duration': format_duration(duration),
            }
        non_closed_visits.append(non_closed_visit)
        context = {
            'non_closed_visits': non_closed_visits,
        }
    return render(request, 'storage_information.html', context)
