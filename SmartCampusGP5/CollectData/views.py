# from . import iot_mqtt
from .models import Data
from django.db.models import Count
from .forms import DataForm
from django.shortcuts import redirect, render
from django.views import generic

from django.core.paginator import Paginator

# Create your views here.
def index(request):
    data = Data.objects.all()

    if request.method == "POST":
        form = DataForm(request.POST)
        if form.is_valid():
            loc = form.cleaned_data.get("loc")
            if loc == "null":
                data = Data.objects.all()
            else:
                data = Data.objects.filter(loc=loc)
    #         # if loc not "":
    #         #     data = Data.objects.filter(loc = loc)
    #         # else:
    #         #     data = Data.objects.all()
    else:
        form = DataForm()

    p = Paginator(data, 50)
    page_number = request.GET.get("page")
    page_obj = p.get_page(page_number)

    context = {
        "form": form,
        "page_number": page_number,
        "page_obj": page_obj,
    }
    return render(request, "data.html", context=context)


class DataListView(generic.ListView):
    model = Data

    context_object_name = "my_data_list"
    queryset = Data.objects.all()
    template_name = "data.html"

    p = Paginator(queryset, 50)
