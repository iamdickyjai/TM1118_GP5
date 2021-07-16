from CollectData.models import Data
from .models import Event
from django.core.mail import send_mail
from django.utils import timezone
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()
scheduler.start()

def EventDetect():
    venue_list = Data.objects.values("loc").order_by("loc").distinct()
    venues = []
    for venue in venue_list:
        venues.append(venue["loc"])

    msg = ""
    for loc in venues:
        last_data = Data.objects.all().filter(loc=loc).order_by("-date_created")[:1][0]
        if last_data.light >= 40:
            #print("{} has people using now!".format(last_data.loc))
            events = Event.objects.all().filter(venue=loc)
            found = False
            for event in events:
                if event.time_start <= last_data.date_created <= event.time_end:
                    found = True
                    break
            if not found:
                msg += "{} work at unscheduled time!\n".format(last_data.loc)
                #print(msg)
    if msg != "":
        send_mail("Smart Campus GP5 Alert", msg, "None", ["paak-ho.tse@connect.polyu.hk"], fail_silently=False)
    print("Room Checked")

EventDetect()
scheduler.add_job(EventDetect, "interval", hours=1)
#scheduler.add_job(EventDetect, "interval", minutes=1)