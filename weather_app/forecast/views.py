from django.shortcuts import render
from django.http import HttpResponse

import requests 
from django.conf import settings


# LOGIC GOES HERE 
def home(request):
    return HttpResponse("Hello, Weather App!")

