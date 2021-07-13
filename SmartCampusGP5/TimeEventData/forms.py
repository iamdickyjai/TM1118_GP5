from django import forms
from CollectData.models import Data
from VenueEvent.models import Event

class TimeEventForm(forms.Form):
    data = Data.objects.all()
    event = Event.objects.all()
    venue = []
    for datum in data:
        skip = False
        for item in venue:
            if datum.loc == item:
                skip =True
                break
        if not skip:
            venue.append(datum.loc)
    for datum in event:
        skip = False
        for item in venue:
            if datum.venue == item:
                skip =True
                break
        if not skip:
            venue.append(datum.venue)

    tup = ()
    for item in venue:
        tup = tup + ((item, item),)
    
    VENUE_CHOICES = tup
    venue = forms.ChoiceField(choices=VENUE_CHOICES)
    start_time = forms.DateTimeField()
    end_time = forms.DateTimeField()