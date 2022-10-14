from rest_framework.generics import ListAPIView
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.filters import SearchFilter
# Create your views here.

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [SearchFilter]
    # search_fields = ['city']
    # search_fields = ['name','city']
    search_fields = ['^name']





    