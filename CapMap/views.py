from django.shortcuts import render
from django.http import HttpResponse


def map_view(request):
    return HttpResponse('Map Page')

