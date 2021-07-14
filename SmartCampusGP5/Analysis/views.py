from CollectData.models import Data
from django.db.models import Count, Avg
from django.shortcuts import redirect, render
import math

# Create your views here.
def index(request):
    venueR = Data.objects.values_list('loc').annotate(most = Count("loc")).order_by("most")
    max_venue = ("", 0)
    for venue in venueR:
        if max_venue[0] == "":
            max_venue = venue
        else:
            if venue[1] > max_venue[1]:
                max_venue = venue

    venue_group_by_temp = Data.objects.values_list('loc').annotate(temp = Avg("temp")).order_by("temp")

    temp_list = []
    for datum in venue_group_by_temp:
        temp_list.append((datum[0], math.floor(datum[1] * 100) / 100))

    venue_group_by_temp = temp_list

    context = {
        'max_venue': max_venue,
        "venue_group_by_temp": venue_group_by_temp,
    }
    return render(request, "analysis.html", context = context)