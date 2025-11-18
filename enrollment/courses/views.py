from django.shortcuts import render
from django.http import HttpResponse

def course(request):
    return HttpResponse("""BSIT \nBSPA \n BSE \n BSA \n BSAIS \n BTVTED \n DHRS \n BSPA""")


def course_page(request, name):
    return HttpResponse(f'This is the homepage of {name} course ')