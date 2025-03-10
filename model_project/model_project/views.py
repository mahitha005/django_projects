from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

def add_student(request):
    # Check if the user clicked the button (optional safeguard)
    if request.method == "GET":
        # Student details (Modify as needed)
        student_data = {
            "name": "John Doe",
            "email": "johndoe@example.com",
            "age": 20
        }

        # Insert into the database, ensuring no duplicate emails
        if not Student.objects.filter(email=student_data["email"]).exists():
            Student.objects.create(**student_data)
            message = f"Student {student_data['name']} added successfully!"
        else:
            message = "Student with this email already exists!"

        return render(request, "add_student.html", {"message": message})