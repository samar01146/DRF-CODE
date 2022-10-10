from django.shortcuts import render
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.

# model object - single student data
def Student_detail(request, pk):
    stu = Student.objects.get(id=pk)  #complex data in Queryset/model instance
    # print(stu)
    serializer = StudentSerializer(stu) # convert it in Python Object
    # print(serializer)
    # print(serializer.data)
    json_data = JSONRenderer().render(serializer.data) # convert it in Json Format
    # print(json_data)
    return HttpResponse(json_data , content_type= 'application/json')

# model object - many Student data
def Student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
    
