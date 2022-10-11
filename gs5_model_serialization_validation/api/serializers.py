from dataclasses import field
from rest_framework import serializers
from api.models import Student

#validators with field
    



class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)
    class Meta:
        model = Student
        fields = ['id', 'name' , 'roll' , 'city'] 
