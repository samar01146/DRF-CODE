from csv import field_size_limit
from rest_framework import serializers
from api.models import Student

class StudentSerialization(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id' , 'name' , 'roll' , 'city']