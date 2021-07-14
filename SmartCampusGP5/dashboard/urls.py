from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="dashboard"),
    # path('test', views.test, name='test'),
    #path('temp_data/<slug:venue>/', views.temp_data, name='temp_data'),
    #path(r'^temp_data/(?P<venue>\w+)/$', views.temp_data, name='temp_data'),
    path('temp_data', views.temp_data, name='temp_data'),
]