from rest_framework import serializers
from api.models import Student
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length= 100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length= 100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instanse, validated_data):
        instanse.name = validated_data.get('name', instanse.name)
        instanse.roll = validated_data.get('roll', instanse.roll)
        instanse.city = validated_data.get('city', instanse.city)
        instanse.save()
        return instanse 
    
    
