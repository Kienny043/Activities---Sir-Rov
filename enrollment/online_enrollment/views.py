from .models import Student, Course, Enrollment, Instructor, Subject
from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm, InstructorForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegisterForm

# Create your views here.


def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

# def course_list(request):
#     courses = Course.objects.all()
#     return render(request, "course_list.html",{"courses": courses})


# def enrollment_list(request):
#     enrollments = Enrollment.objects.all()
#     return render(request, "enrollment_list.html",{"enrollments": enrollments})

def instructor_list(request):
    instructors = Instructor.objects.all()
    return render(request, "instructors/instructor_list.html",{"instructors": instructors})

# def subject_list(request):
#     subjects = Subject.objects.all()
#     return render(request, "subject_list.html",{"subjects": subjects})

def add_student(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'students/add_student.html', {'form': form})


def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'students/edit_student.html', {'form': form, 'student': student})


def add_instructor(request):
    form = InstructorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('instructor_list')
    return render(request, 'instructors/add_instructor.html', {'form': form})

def edit_instructor(request, pk):
    instructor = get_object_or_404(Instructor, pk=pk)
    form = InstructorForm(request.POST or None, instance=instructor)
    if form.is_valid():
        form.save()
        return redirect('instructor_list')
    return render(request, 'instructors/edit_instructor.html', {'form': form, 'instructor': instructor})


def register_user(request):
    if request.method == "POST":
        form =RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account Created Successfully! You can now log in.")
            return redirect('login_user')
        else:
            messages.error(request,"Please correct the errors below.")
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', { 'forms': form })

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,f"Welcome back, {username}!")
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form' : form })

def logout_user(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login_user')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')