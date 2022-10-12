from .models import Student
from .serializers import StudentSerialization
from rest_framework.generics import  ListCreateAPIView, RetrieveUpdateDestroyAPIView


class StudentListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialization

class StudentRetriveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialization 