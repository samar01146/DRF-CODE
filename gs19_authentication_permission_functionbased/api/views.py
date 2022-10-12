from functools import partial
from urllib import response
from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from api.models import Student
from .serializers import StudentSerialization
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['GET', "POST" , 'PUT' , 'DELETE' , 'PATCH'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def student_api(request, id=None):
    if request.method=="GET":
        id = id
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerialization(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerialization(stu, many=True)
        return Response(serializer.data)

    if request.method=="POST":
        data = request.data
        print("===========================================",data)
        serializer = StudentSerialization(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Data Created'} , status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    if request.method =="PUT":
        data = request.data
        id = id
        stu = Student.objects.get(id=id)
        serializer = StudentSerialization(stu ,data=data ,  partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Data updated'})
        return Response(serializer.errors)
    
    if request.method == 'DELETE':
        id = id
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'msg' : 'Data Deleted'})

    