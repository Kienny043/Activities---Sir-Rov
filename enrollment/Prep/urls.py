from django.urls import path
from . import views

urlpatterns = [
    path('', views.people, name= 'list of people')
]