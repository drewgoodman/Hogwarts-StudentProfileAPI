from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from students.models import Student, Course, Enrollment, Grade
from .serializers import StudentSerializer, CourseSerializer


# Create your views here.

@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'Student List': '/students/',
        'Course List': '/courses/'
    }
    return Response(api_urls)

@api_view(['GET'])
def student_list(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def courses_list(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)