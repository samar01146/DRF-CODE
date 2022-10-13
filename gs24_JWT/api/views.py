from .models import Student
from .serializers import StudentSerialization
from rest_framework import viewsets
# from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication



class StudentModelViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerialization
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]



