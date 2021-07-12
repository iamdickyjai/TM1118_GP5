from django.shortcuts import render
from . import iot_mqtt
from .models import Data
from django.db.models import Count

# Create your views here.
def index(request):
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
    context={
        'data': data,
        'avail_venue': venue,
    }
    return render(request, "data.html", context = context)
