from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser

from CRUD_API.api.models import Student
from . serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def student_create(request):
    if request.method == "POST":
        json_data = request.body # it takes from myapp.py
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>",request.body)
        stream = io.BytesIO(json_data) # convert it into stream
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>",stream)

        pythondata = JSONParser().parse(stream) # convert it into native python type
        print("??????????????????????", pythondata)
        serializer = StudentSerializer(data = pythondata) # it cnvert it into Python object to complex data
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>' , serializer)
        if serializer.is_valid():
            serializer.save()
            res = {'msg' : 'Data Created' }
            json_data = JSONRenderer().render(res) # it coverts python object to Jsondata
            return HttpResponse(json_data, content_type = 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json')
    
