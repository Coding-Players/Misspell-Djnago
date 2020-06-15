from django.urls import path
from . import views


urlpatterns = [
    path('', views.map_view, name='Map_Page'),
    path('Add_Location/', views.add_location, name='Add_Location'),
]
