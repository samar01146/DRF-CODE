from urllib import response
from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerialization
from rest_framework import status
from rest_framework import viewsets


class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        stu = Student.objects.all()
        serializer = StudentSerialization(stu, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        id = pk 
        if id is not None:
            stu = Student.objects.get(pk=id)
            serializer = StudentSerialization(stu)
            return Response(serializer.data)
    
    def create(self, request):
        data = request.data
        serializer = StudentSerialization(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : "data created"} , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        id = pk
        stu = Student.objects.get(pk=id)
        data =request.data
        serializer = StudentSerialization(stu , data=data)
        if serializer.is_valid():
            serializer.save()
            return response({'msg' : "Data Updated"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk):
        id = pk
        stu = Student.objects.get(pk=id)
        data = request.data
        serializer = StudentSerialization(stu, data=data , partial =True)
        if serializer.is_valid():
            serializer.save()
            return response({'msg' : "partial data updated"})
        return Response(serializer.errors)

    def destroy(self, request, pk):
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg' : 'data deleted'})        

