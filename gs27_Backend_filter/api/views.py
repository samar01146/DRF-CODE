from urllib import request
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from api.models import Student
from api.serializers import StudentSerializer
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends= [DjangoFilterBackend]
    # filterset_fields = ["city" ]
    filterset_fields = ["city" , "name"]


    