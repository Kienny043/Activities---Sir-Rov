from django.urls import path
from . import views


urlpatterns = [
    path('students/', views.student_list, name='student_list'),
    # path("courses/", views.course_list, name="course_list"),
    # path("enrollments/", views.enrollment_list, name="enrollment_list"),
    path("instructors/", views.instructor_list, name="instructor_list"),
    # path("subjects/", views.subject_list, name="subject_list"),
    path('students/add/', views.add_student, name='add_student'),
    path('students/edit/<int:pk>/', views.edit_student, name='edit_student'),
    path('instructors/add/', views.add_instructor, name='add_instructor'),
    path('instructors/edit/<int:pk>/', views.edit_instructor, name='edit_instructor'),
    path('register/', views.register_user, name='register_user'),
    path('login/', views.register_user, name='login_user'),
    path('logout/', views.register_user, name='logout_user'),
    path('dashboard/', views.register_user, name='dashboard'),
]