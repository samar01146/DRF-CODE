from .models import Student
from .serializers import StudentSerialization
from rest_framework import viewsets


class StudentModelViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerialization