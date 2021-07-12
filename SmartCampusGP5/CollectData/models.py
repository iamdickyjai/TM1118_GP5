from django.db import models

# Create your models here.
class Data(models.Model):
    node_id = models.CharField(help_text = "The id of the node", max_length= 10)
    loc = models.CharField(help_text = "The location of the node", max_length=6)
    temp = models.DecimalField(decimal_places = 1, max_digits=5)
    hum = models.DecimalField(decimal_places = 1, max_digits=5)
    light = models.DecimalField(decimal_places = 1, max_digits=5)
    snd = models.DecimalField(decimal_places = 1, max_digits=5)
    date_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.node_id