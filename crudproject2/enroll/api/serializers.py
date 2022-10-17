from  rest_framework import serializers
from enroll.models import User

class UserSerialization(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id' ,'name' , 'email' , 'password']