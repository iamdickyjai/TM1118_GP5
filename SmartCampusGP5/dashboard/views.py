from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from CollectData.models import Data
from .forms import DashboardForm
from django.utils import timezone

venue = [""]

# Create your views here.
def index(request):
    global venue

    if request.method == "POST":
        form = DashboardForm(request.POST)
        context = {
            "form": form,
        }
        if form.is_valid():
            form_venue = form.cleaned_data["venue"]
            print(form_venue)
            if form_venue != "null":
                venue = form_venue
    else:
        form = DashboardForm()
        context = {
            "form": form,
        }
        venue = [""]

    return render(request, 'dashboard/dashboard.html', context)

def temp_data(request):
    one_h_ago = timezone.now()-timezone.timedelta(hours=1)
    #events = Data.objects.filter(loc__in=venue).filter(date_created__gte=one_h_ago)
    events = Data.objects.filter(date_created__gte=one_h_ago)
    if "all" not in venue:
        events = events.filter(loc__in=venue)
    data = serializers.serialize('json', events) #Translating Django models into JSON formats
    return JsonResponse(data, safe=False) #Returns a string that contains an array object
