from . import iot_mqtt
from . import m5_mqtt as yoyo
from django.http.response import JsonResponse
from .models import Data
from django.db.models import Count
from .forms import DataForm
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.http import HttpResponse
import json

data = Data.objects.all()

def alert(request):
    alert = yoyo.alert
    if alert:
        message = "The object is moved!"
    else:
        message = "Nothing :)"
    print(message)
    test = {"alert_result": message}
    return JsonResponse(test)

# Create your views here.
def index(request):
    context = {}
    global data
    p = Paginator(data, 50)

    if request.method == "POST":
        form = DataForm(request.POST)
        if form.is_valid():
            loc = form.cleaned_data.get("loc")
            if loc == "null":
                data = Data.objects.all()
                p = Paginator(data, 50)
            else:
                data = Data.objects.filter(loc=loc)
                p = Paginator(data, 50)
        context["form"] = form

        page_number = 1
        context['page_number'] = page_number
        
        total_page = p.num_pages
        context['total_page'] = total_page      

        page_obj = p.get_page(page_number)
        
        has_next = page_obj.has_next()
        has_previous = page_obj.has_previous()
        context['has_next'] = has_next
        context["has_previous"] = has_previous

        if has_next:
            context['next_page_number'] = page_obj.next_page_number()
            context['end_index'] = page_obj.end_index()
        if has_previous:
            context['previous_page_number'] = page_obj.previous_page_number()
            context['start_index'] = page_obj.start_index()

        

        page_list = []
        for page_record in page_obj:
            record = {}
            record['id'] = page_record.id
            record['node_id'] = page_record.node_id
            record['loc'] = page_record.loc
            record['temp'] = page_record.temp
            record['hum'] = page_record.hum
            record['light'] = page_record.light
            record['snd'] = page_record.snd
            record['date_created'] = page_record.date_created
            page_list.append(record)

        context['page_list'] = page_list
        # context['page_obj'] = page_obj
        return render(request, "data.html", context=context)


    if request.method == "GET":
        if request.GET.get("page_no"):
            print("GET PAGE NO")
            page_number = request.GET.get("page_no")
            context['page_number'] = page_number
            
            total_page = p.num_pages
            context['total_page'] = total_page      

            page_obj = p.get_page(page_number)
            
            has_next = page_obj.has_next()
            has_previous = page_obj.has_previous()
            context['has_next'] = has_next
            context["has_previous"] = has_previous

            if has_next:
                context['next_page_number'] = page_obj.next_page_number()
                context['end_index'] = len(page_obj.object_list)
            if has_previous:
                context['previous_page_number'] = page_obj.previous_page_number()

            page_list = []
            for page_record in page_obj:
                record = {}
                record['id'] = page_record.id
                record['node_id'] = page_record.node_id
                record['loc'] = page_record.loc
                record['temp'] = page_record.temp
                record['hum'] = page_record.hum
                record['light'] = page_record.light
                record['snd'] = page_record.snd
                record['date_created'] = page_record.date_created
                page_list.append(record)
            
            # page_list = [{'id': xxx, 'node_id": yyy .....}, {}, {} ...]
            context["page_list"] = page_list
            return JsonResponse(context)
        else:
            form = DataForm()
            context['form'] = form
            data = Data.objects.all()
            p = Paginator(data, 50)
        
        
        page_number = 1
        context['page_number'] = page_number
        
        total_page = p.num_pages
        context['total_page'] = total_page      

        page_obj = p.get_page(page_number)
        
        has_next = page_obj.has_next()
        has_previous = page_obj.has_previous()
        context['has_next'] = has_next
        context["has_previous"] = has_previous

        if has_next:
            context['next_page_number'] = page_obj.next_page_number()
            context['end_index'] = page_obj.end_index()
        if has_previous:
            context['previous_page_number'] = page_obj.previous_page_number()
            context['start_index'] = page_obj.start_index()

        page_list = []
        for page_record in page_obj:
            record = {}
            record['id'] = page_record.id
            record['node_id'] = page_record.node_id
            record['loc'] = page_record.loc
            record['temp'] = page_record.temp
            record['hum'] = page_record.hum
            record['light'] = page_record.light
            record['snd'] = page_record.snd
            record['date_created'] = page_record.date_created
            page_list.append(record)

        context['page_list'] = page_list

        # If not reqeust from AJAX, return the whole html
        return render(request, "data.html", context = context)
    








    # page_number = request.GET.get("page_no")
    # context["page_number"] =  page_number
    # page_obj = p.get_page(page_number)
    # context["page_obj"] =  page_obj


