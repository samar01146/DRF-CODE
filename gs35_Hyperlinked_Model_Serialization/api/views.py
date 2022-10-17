from django.shortcuts import render
from api.models import Student
from api.serializers import Studentserializer
from rest_framework import viewsets

# Create your views here.
class StudentModelView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class =Studentserializer