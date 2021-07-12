from django.contrib import admin
from .models import Data

# Register your models here.
@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ("id", "node_id", "loc", "temp", "hum", 'light', 'snd', 'date_created')