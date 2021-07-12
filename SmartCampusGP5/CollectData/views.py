from django.shortcuts import render
from . import iot_mqtt
from .models import Data

# Create your views here.
def index(request):
    data = Data.objects.all()
    context={
        'data': data,
    }
    return render(request, "data.html", context = context)
