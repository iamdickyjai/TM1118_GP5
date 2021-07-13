from django.shortcuts import render, redirect
from CollectData.models import Data
from VenueEvent.models import Event
from .forms import TimeEventForm
from datetime import datetime
from django.db.models import Q

# Create your views here.
def search(request):
    if request.method=="POST":
        form = TimeEventForm(request.POST)
        context = {'form': form,}
        if form.is_valid():
            venue = form.cleaned_data["venue"]
            form_start_time = form.cleaned_data["start_time"]
            form_end_time = form.cleaned_data["end_time"]
        
            event_data = Event.objects.filter(Q(time_start__range = (form_start_time, form_end_time)) | Q(time_end__range = (form_start_time, form_end_time)))
            envir_data = Data.objects.filter(date_created__range=(form_start_time, form_end_time))

            context = {
                "form" : form,
                'event': event_data,
                'envir': envir_data,
            }
    else:
        form = TimeEventForm()
        context = {
            "form": form,
        }

    return render(request, 'search.html', context)
    # return render(request, 'search.html')

    # events = Event.objects.all()
    # list_event = []
    # for e in events:
    #     event_start_time = e.display_start_datetime
    #     event_end_time = e.display_end_datetime
    #     event_id = e.id
    #     dic = {}
    #     dic['id'] = event_id
    #     dic['start'] = event_start_time
    #     dic['end'] = event_end_time
    #     list_event.append(dic)


    # # "t": list_event[0]['start'],
    # context = {
    #     "t": list_event[0]['start'],
    # }

    # return render(request, "test.html", context)