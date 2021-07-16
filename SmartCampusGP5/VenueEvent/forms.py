from django import forms
from django.forms import ModelForm
from django.forms.widgets import DateTimeInput
from .models import Event
from CollectData.models import Data

class SearchEventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('venue',)
        venue_list = Event.objects.values("venue").order_by("venue").distinct()
        venues = []
        for venue in venue_list:
            venues.append(venue["venue"])
        
        tup = (("null", "------All------"), )
        for item in venues:
            tup = tup + ((item, item),)

        VENUE_CHOICES = tup
        widgets = {'venue': forms.Select(choices=VENUE_CHOICES)}

class AddEventForm(ModelForm):
    class Meta:
        model = Event
        fields = "__all__"

        venue_list = Data.objects.values("loc").order_by("loc").distinct()
        venues = []
        for venue in venue_list:
            venues.append(venue["loc"])
        
        tup = ()
        for item in venues:
            tup = tup + ((item, item),)

        VENUE_CHOICES = tup
        
        widgets = {
            "venue": forms.Select(choices=VENUE_CHOICES),
            "time_start": DateTimeInput(attrs={"type": "datetime-local"}),
            "time_end": DateTimeInput(attrs={"type": "datetime-local"})
        }