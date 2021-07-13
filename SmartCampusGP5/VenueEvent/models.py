from django.db import models
from datetime import datetime

# Create your models here.
class Event(models.Model):
    venue = models.CharField(max_length= 10)
    # date = models.DateField()
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    event = models.CharField(max_length= 20)
    instructor = models.CharField(max_length= 30)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.id)

    # def display_start_datetime(self):
    #     return datetime.combine(self.date, self.time_start)
    
    # def display_end_datetime(self):
    #     return datetime.combine(self.date, self.time_end)
