from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def register(request):
    return HttpResponse('Are you registered yet?')

def registration_form(request):
    return HttpResponse("There's suppose to be a form here, but di ko alam kung pano gawin")