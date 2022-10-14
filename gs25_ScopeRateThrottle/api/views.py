from .models import Student
from .serializers import StudentSerialization
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.throttling import ScopedRateThrottle


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialization
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'viewstu'

class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialization
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modify'


class StudentRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialization
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'viewstu'
    throttle_scope = 'modify'

class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialization
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modify'

class StudentDestroy(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialization
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modify'


