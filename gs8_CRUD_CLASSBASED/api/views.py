from ast import Delete
from functools import partial
from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Student
from .serializers import StudentSerialization
from rest_framework import status

# Create your views here.

class StudentAPI(APIView):
    def get(self, request, id=None, format=None):
            id = id
            if id is not None:
                stu = Student.objects.get(id=id)
                serializer = StudentSerialization(stu)
                return Response(serializer.data)
            stu = Student.objects.all()
            serializer = StudentSerialization(stu, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
            data = request.data 
            print("===========================================",data)
            serializer = StudentSerialization(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg' : 'Data Created'} , status=status.HTTP_201_CREATED)
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id, format=None):
            id = id
            stu = Student.objects.get(id=id)
            data = request.data
            serializer = StudentSerialization(stu ,data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg' : 'Data updated'})
            return Response(serializer.errors ,  status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id, format=None):
            id = id
            stu = Student.objects.get(id=id)
            data = request.data
            serializer =StudentSerialization(stu, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg' : "partial Data Updated"})
            return Response(serializer.errors ,  status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self , request , id , format=None):
            id = id
            stu = Student.objects.get(id=id)
            stu.delete()
            return Response({'msg' : 'Data Deleted'})

    