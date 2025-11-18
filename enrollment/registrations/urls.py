from django.urls import path
from . import views

urlpatterns = [
    path('registrations/',views.register, name='registration'),
    path('registrations/form',views.registration_form, name='registration_form'),
]