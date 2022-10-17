from django.shortcuts import render
from .serielizers import StudentSerializer
from .models import Student
from rest_framework.generics import ListAPIView
from api.pagination import MyCursorPagination

# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyCursorPagination 