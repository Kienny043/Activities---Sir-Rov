from django import forms
from .models import Student, Instructor
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'first_name', 'last_name', 'phone', 'email']
        widgets = {
            'student_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Student ID'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email Address'}),
        }

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['instructor_id', 'name', 'department', 'phone', 'email']
        widgets = {
            'instructor_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Instructor ID'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Full Name'}),
            'department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Department'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email Address'}),
        }



class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text = 'Required. Enter a valid Email Address.')

    class META:
        model = User
        fields = ['username', 'email', 'password1', 'password2']