from rest_framework import serializers

from students.models import Student, Course, Enrollment, Grade, Tag

class StudentSerializer(serializers.ModelSerializer):

    courses = serializers.SerializerMethodField(read_only=True)
    tags = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Student
        fields = ['id','firstName','lastName','skill','house','currentYear','enrollDate','image','courses','tags']

    def get_courses(self, obj):
        courses = obj.enrollment_set.all()
        serializer = EnrollmentSerializer(courses, many=True)
        return serializer.data

    def get_tags(self, obj):
        tags = obj.tag_set.all()
        serializer = TagSerializer(tags, many=True)
        return serializer.data

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ['name']


class EnrollmentSerializer(serializers.ModelSerializer):

    name = serializers.CharField(source="course.name")
    grades = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Enrollment
        fields = ['name','grades','id']

    def get_grades(self, obj):
        grades = obj.grade_set.all()
        serializer = GradeSerializer(grades, many=True)
        return serializer.data


class GradeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Grade
        fields = ['grade','date','id']


class TagSerializer(serializers.ModelSerializer):
    def to_representation(self, obj):
        return obj.name