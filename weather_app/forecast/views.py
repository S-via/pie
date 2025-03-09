from django.shortcuts import render
from django.http import HttpResponse


# LOGIC GOES HERE 
def home(request):
    return HttpResponse("Hello, Weather App!")

