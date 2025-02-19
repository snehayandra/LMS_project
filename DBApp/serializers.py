from rest_framework import serializers
from . import models

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = '__all__'  # Corrected 'full_name'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models. Student
        fields = '__all__'     
