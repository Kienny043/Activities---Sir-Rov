from django.urls import path
from . import views

urlpatterns = [
    path('student/<str:name>',views.student_info, name='students_page'),
    path('student/',views.student, name='not yet a student'),
]