from django.shortcuts import render
from django.http import HttpResponse


def map_view(request):
    return HttpResponse('Map page')
# <a href="/">Back</a></br><h1>This is map page</h1>
