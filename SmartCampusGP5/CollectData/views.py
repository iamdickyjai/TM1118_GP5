from django.shortcuts import render
from . import iot_mqtt
from .models import Data

# Create your views here.
def index(request):
    return render(request, "data.html")
