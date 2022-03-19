from student.models import Student
from rest_framework import generics
from student.serializers import StudentSerializer
# Create your views here.
class ListCreateStudent(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class UpdateDestroyStudent(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer