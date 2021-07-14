from django import forms
from django.forms import ModelForm
from CollectData.models import Data
from multiselectfield import MultiSelectFormField
from django.db.models import Count


class DashboardForm(forms.Form):
    data = Data.objects.all().order_by("loc")
    data2 = (
        Data.objects.values_list("loc")
        .annotate(location=Count("loc"))
        .order_by("location")
    )
    venue_no = data2.count()
    venue = []
    for datum in data:
        skip = False
        for item in venue:
            if datum.loc == item:
                skip = True
                break
        if not skip:
            venue.append(datum.loc)

    tup = (("all", "All"),)
    # tup = ()
    for item in venue:
        tup = tup + ((item, item),)

    VENUE_CHOICES = tup
    venue = forms.MultipleChoiceField(
        choices=VENUE_CHOICES, widget=forms.CheckboxSelectMultiple()
    )
