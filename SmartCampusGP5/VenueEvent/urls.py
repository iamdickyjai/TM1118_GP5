from django.urls import path
from . import views

urlpatterns = [
    path("", views.add, name="addEvent"),
    path("readExcel/", views.readExcel),
]