from django.shortcuts import render, redirect
from django.contrib import messages  # Import messages
from .models import Student

def insert_student(request):
    if request.method == "POST":  
        student = Student(name="G_R_Mahitha", age=20, email="mahitha2005.mahi@gmail.com")
        student.save()
        messages.success(request, "Student record added successfully!")  # Add success message
    return redirect('student_list')  # Redirect to refresh the page

def student_list(request):
    students = Student.objects.all()  # Fetch all students
    return render(request, 'modelsapp/student_list.html', {'students': students})
