from urllib import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

# @api_view()
# def hello_world(request):
#     return Response({'msg': 'Hello World' })

# @api_view(['GET'])
# def hello_world(request):
#     return Response({'msg': 'Hello World' })

@api_view(['GET','POST'])
def hello_world(request):
    if request.method == "GET":
        return Response({'msg' : "THis is your GET method"})

    if request.method == "POST":
        print(request.data)
        return Response({'msg' : "THis is your POST method" , 'data' : request.data})