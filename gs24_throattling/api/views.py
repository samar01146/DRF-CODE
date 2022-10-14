from .models import Student
from .serializers import StudentSerialization
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from api.throttling import JackRateThrottle

class StudentModelViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerialization
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    # throttle_classes =[JackRateThrottle ,UserRateThrottle]
    throttle_classes =[JackRateThrottle ,AnonRateThrottle]




