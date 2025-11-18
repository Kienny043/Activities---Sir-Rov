from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

 
class Instructor(models.Model):
    instructor_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    course_id = models.CharField(max_length=100, unique=True)
    course_name = models.CharField(max_length=100)
    units = models.IntegerField()
    description = models.TextField()
    duration = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    duration = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.student} enrolled in {self.course}"
class Subject(models.Model):
    subject_id = models.CharField(max_length=100, unique=True)
    subject_name = models.CharField(max_length=100)
    units = models.IntegerField()
    schedule = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)

    def __str__(self):
        return self.subject_name
