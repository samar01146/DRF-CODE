from .models import Student
from .serializers import StudentSerialization
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from api.custompermissions import MyPermission

class StudentModelViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerialization
    authentication_classes = [SessionAuthentication]
    permission_classes = [MyPermission]



