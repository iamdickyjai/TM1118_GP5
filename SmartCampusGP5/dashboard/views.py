from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from CollectData.models import Data
from .forms import DashboardForm
from django.utils import timezone

venue = []

# Create your views here.
def index(request):
    global venue
    form = DashboardForm()

    if request.method == "POST":
        context = {
            "form": form,
        }
        venue = []
        for x in range(0, form.venue_no):
            result_form_web = request.POST.get("id_venue_{}".format(x))
            if result_form_web:
                venue.append(result_form_web)
            print(venue)
        # if form.is_valid():
        #     form_venue = form.cleaned_data["venue"]
        #     if form_venue != "null":
        #         venue = form_venue
    else:
        context = {
            "form": form,
        }
        venue = []

    return render(request, "dashboard/dashboard.html", context)


def temp_data(request):
    # one_h_ago = timezone.now() - timezone.timedelta(hours=72)
    # events = Data.objects.filter(loc__in=venue).filter(date_created__gte=one_h_ago)
    # events = Data.objects.filter(date_created__gte=one_h_ago)
    events = Data.objects.all()[:100]
    if "All" not in venue:
        events = Data.objects.filter(loc__in=venue)[:100]
    data = serializers.serialize(
        "json", events
    )  # Translating Django models into JSON formats
    return JsonResponse(
        data, safe=False
    )  # Returns a string that contains an array object
