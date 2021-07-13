from django.shortcuts import render

from . import iot_mqtt
from .models import Data
from django.db.models import Count
from .forms import DataForm
from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    data = Data.objects.all()
    # venue = []
    # for datum in data:
    #     skip = False
    #     for item in venue:
    #         if datum.loc == item:
    #             skip = True
    #             break
    #     if not skip:
    #         venue.append(datum.loc)
    
    if request.method == "POST":
        form = DataForm(request.POST)
        if form.is_valid():
            loc = form.cleaned_data.get("loc")
            if(loc == "null"):
                data = Data.objects.all()
            else:
                data = Data.objects.filter(loc = loc)
    #         # if loc not "":
    #         #     data = Data.objects.filter(loc = loc)
    #         # else:
    #         #     data = Data.objects.all()
    else:
        form = DataForm()
    
    context = {
        "data": data,
        'form': form,
    }
    return render(request, "data.html", context=context)
