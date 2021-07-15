from django.shortcuts import render
from .models import Event
import os, pandas as pd
import xlrd
import datetime

# Create your views here.
def index(request):
    return render(request, "event.html")

def readExcel(request):
    
    df = pd.read_excel("Venue-Event.xlsx")

    for x in range(1, len(df)):
        events = Event()
        events.venue = df.loc[x, df.columns[0]].upper()
        # events.date =  str(datetime.datetime.strptime(
        #     str(df.loc[x, df.columns[1]]), "%Y-%m-%d %H:%M:%S"
        # ).date())
        # events.time_start = df.loc[x, df.columns[2]]
        # events.time_end = df.loc[x, df.columns[3]]
        events_date =  datetime.datetime.strptime(str(df.loc[x, df.columns[1]]), "%Y-%m-%d %H:%M:%S")

        events.time_start = datetime.datetime.combine(events_date, df.loc[x, df.columns[2]])
        events.time_end = datetime.datetime.combine(events_date, df.loc[x, df.columns[3]])
        events.event = df.loc[x, df.columns[4]]
        events.instructor = df.loc[x, df.columns[5]]
        events.save()

    return render(request, "excel.html")