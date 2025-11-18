from django.shortcuts import render
from .models import person
# Create your views here.

def people(request):
    peeps = person.objects.all()
    return render(request, 'person.html', {'peeps' : peeps})