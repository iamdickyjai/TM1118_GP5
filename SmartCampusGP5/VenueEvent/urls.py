from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="event"),
    path("readExcel/", views.readExcel),
]