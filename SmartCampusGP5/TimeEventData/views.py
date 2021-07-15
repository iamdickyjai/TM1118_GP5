from django.shortcuts import render, redirect
from CollectData.models import Data
from VenueEvent.models import Event
from .forms import TimeEventForm
from datetime import datetime
from django.db.models import Q, Avg

# Create your views here.
def search(request):
    if request.method == "POST":
        form = TimeEventForm(request.POST)
        context = {
            "form": form,
        }
        if form.is_valid():
            venue = form.cleaned_data["venue"]
            form_start_time = form.cleaned_data["start_time"]
            form_end_time = form.cleaned_data["end_time"]
            event_data = Event.objects.filter(
                Q(time_start__range=(form_start_time, form_end_time))
                | Q(time_end__range=(form_start_time, form_end_time))
            )
            event_data = event_data.filter(venue__exact=venue)

            # The code to get the time range of data database
            # envir_data = Data.objects.filter(date_created__range=(form_start_time, form_end_time))
            # envir_data = envir_data.filter(loc__exact = venue)
            avg_temp_list = []
            avg = ""
            for datum in event_data:
                avg = Data.objects.filter(
                    Q(date_created__range=(datum.time_start, datum.time_end)),
                    Q(loc=datum.venue),
                ).aggregate(Avg("temp"))
                if avg != "":
                    avg_temp_list.append((datum, avg))

            context = {
                "form": form,
                # "event": event_data,
                "event": avg_temp_list,
                'count': str(len(avg_temp_list)),
            }
    else:
        form = TimeEventForm()
        context = {
            "form": form,
        }

    return render(request, "search.html", context)