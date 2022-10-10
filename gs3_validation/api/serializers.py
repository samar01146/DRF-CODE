from rest_framework import serializers
from api.models import Student

#validators with field
def Start_with_r(value):
    if value[0].lower() != "r":
        raise serializers.ValidationError("Name Should be Start with R")
    



class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length= 100, validators=[Start_with_r])
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

    #Full validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value
    
    #object validation
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'gaurav' and ct.lower() != 'rajkot':
            raise serializers.ValidationError('city must be rajkot')
        return data
