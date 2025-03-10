# students/urls.py
'''from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                # Home page
    path('insert/', views.insert_student, name='insert_student'),  # To insert a student
    path('list/', views.student_list, name='student_list'),         # To view student list
    path('list/', views.student_list, name='student_list')

]'''

from django.urls import path
from .views import student_list, insert_student

urlpatterns = [
    path('', student_list, name='student_list'),
    path('insert/', insert_student, name='insert_student'),
]

