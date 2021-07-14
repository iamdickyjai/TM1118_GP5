from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="dashboard"),
    path('temp_data', views.temp_data, name='temp_data'),
]