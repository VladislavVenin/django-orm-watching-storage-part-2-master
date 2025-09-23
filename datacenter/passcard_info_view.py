from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.utils import get_duration, format_duration, is_visit_long
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    entrances = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for ent in entrances:
        duration = get_duration(ent)
        this_passcard_visit = {
                'entered_at': ent.entered_at,
                'duration': format_duration(duration),
                'is_strange': is_visit_long(ent)
            }
        this_passcard_visits.append(this_passcard_visit)
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
