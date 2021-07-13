from django.forms import ModelForm
from .models import Data
from django import forms

class DataForm(ModelForm):
    class Meta: # Attach additional information
        model = Data
        fields = ('loc',)
        data = Data.objects.all()
        venue = []
        for datum in data:
            skip = False
            for item in venue:
                if datum.loc == item:
                    skip = True
                    break
            if not skip:
                venue.append(datum.loc)
        
        tup = (("null", "------All------"), )
        for item in venue:
            tup = tup + ((item, item),)

        LOC_CHOICES = tup

        widgets = {'loc': forms.Select(choices=LOC_CHOICES)}