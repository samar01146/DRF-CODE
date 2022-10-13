from .models import Student
from .serializers import StudentSerialization
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly,AllowAny


class StudentModelViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerialization
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]



