from django.shortcuts import render
from django.db.models import Count

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from students.models import Student, Course, Enrollment, Grade, Tag
from .serializers import StudentSerializer, CourseSerializer, TagSerializer


# Create your views here.

@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'Student List': '/students/',
        'Student Details': '/students/<id>',
        'Course List': '/courses/',
        'Tags List': '/tags/'
    }
    return Response(api_urls)

@api_view(['GET'])
def student_list(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def student_detail(request, pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(student, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def courses_list(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def tags_list(request):
    tags = Tag.objects.all()
    serializer = TagSerializer(tags, many=True)
    return Response(serializer.data)