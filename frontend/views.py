from django.shortcuts import render

from offenders.models import OffenderProfile


def detail_view(request, uuid):
    data = {}
    offender_profile = OffenderProfile.objects.get(
        id=uuid) or None
    if offender_profile is not None:
        data["offender"] = offender_profile
        data["offense_color"] = "bg-success"
        if offender_profile.is_speeding == True:
            data["offense_color"] = "bg-danger"
    return render(request, "frontend/detail.html", data)
