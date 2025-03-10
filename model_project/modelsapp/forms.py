from django import forms
from .models import Student  # Ensure Student model is correctly imported

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'  # Or specify fields like ['name', 'age', 'grade']
