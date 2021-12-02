from django.shortcuts import render
from django.db.models import Count

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from students.models import Student, Course, Enrollment, Grade, Tag
from .serializers import StudentShallowSerializer, StudentDetailSerializer, CourseShallowSerializer, CourseDetailSerializer, TagSerializer, TagDetailSerializer


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
    students = Student.objects.all().order_by("lastName")
    serializer = StudentShallowSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def student_detail(request, pk):
    student = Student.objects.get(id=pk)
    serializer = StudentDetailSerializer(student, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def courses_list(request):
    courses = Course.objects.all().order_by("name")
    serializer = CourseShallowSerializer(courses, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def course_detail(request, pk):
    course = Course.objects.get(id=pk)
    serializer = CourseDetailSerializer(course, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def tags_list(request):
    tags = Tag.objects.all().order_by("name")
    serializer = TagSerializer(tags, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_tag(request):
    data = request.data
    tag = Tag.objects.create(
        name=data['tagName'],
        student=Student.objects.get(id=data['studentId'])
    )
    serializer= TagDetailSerializer(tag, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_tag(request, pk):
    tag = Tag.objects.get(id=pk)
    tag.delete()
    return Response("Tag Deleted")