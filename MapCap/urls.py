from django.urls import path
from . import views
from MapCap.views import *

path = [
    path('', views.map_view, name="Go_To_Map")
]

