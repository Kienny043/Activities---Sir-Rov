from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def student_info(request, name):
    return HttpResponse(f'my name is {name}, a registered student of DLL')

def student(request):
    return HttpResponse('You are not registered as a student yet. register now!')