from django.urls import path
from . import views

urlpatterns = [
    path('courses/',views.course, name='courses'),
    path('courses/<str:name>',views.course_page, name='course_page'),
]