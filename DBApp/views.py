from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework import generics
from rest_framework import permissions
from django.http import HttpResponse
from rest_framework.views import APIView
from .serializers import TeacherSerializer
from .serializers import StudentSerializer
from . import models

# Create your views here.
def dpprocessing(request):
    if request.method == 'GET':
        return HttpResponse('DB app has received a request')  

class TeacherList(generics.ListCreateAPIView):
    queryset=models.Teacher.objects.all()
    serializer_class=TeacherSerializer
    permission_classes=[permissions.IsAuthenticated]

class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Teacher.objects.all()
    serializer_class=TeacherSerializer 
    permission_classes=[permissions.IsAuthenticated]   

class StudentList(generics.ListCreateAPIView):
    queryset=models.Student.objects.all()
    serializer_class=StudentSerializer
    permission_classes=[permissions.IsAuthenticated]  

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Student.objects.all()
    serializer_class=StudentSerializer 
    permission_classes=[permissions.IsAuthenticated]   