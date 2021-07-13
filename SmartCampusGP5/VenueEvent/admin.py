from django.contrib import admin
from .models import Event

# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("id", "venue", "time_start", "time_end", 'event', 'instructor')