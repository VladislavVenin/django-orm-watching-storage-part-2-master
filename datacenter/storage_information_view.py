from datacenter.models import Visit
from django.shortcuts import render
from datacenter.utils import get_duration, format_duration, is_visit_long


def storage_information_view(request):
    active_visits = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []
    for visit in active_visits:
        duration = get_duration(visit)
        non_closed_visit = {
                'who_entered': visit.passcard,
                'entered_at': visit.entered_at,
                'duration': format_duration(duration),
                'is_strange': is_visit_long(duration)
            }
        non_closed_visits.append(non_closed_visit)
        context = {
            'non_closed_visits': non_closed_visits,
        }
    return render(request, 'storage_information.html', context)
