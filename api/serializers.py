from django.db.models import Count

from rest_framework import serializers

from students.models import Student, Course, Enrollment, Grade, Tag

class StudentShallowSerializer(serializers.ModelSerializer):

    tags = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Student
        fields = ['id','firstName','lastName','birthday','house','status','currentYear','enrollDate','image','tags']

    def get_tags(self, obj):
        tags = obj.tag_set.all().order_by('name')
        serializer = TagSerializer(tags, many=True)
        return serializer.data


class StudentDetailSerializer(serializers.ModelSerializer):

    courses = serializers.SerializerMethodField(read_only=True)
    tags = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Student
        fields = ['id','firstName','lastName','skill','birthday','house','status','currentYear','enrollDate','image','courses','tags']

    def get_courses(self, obj):
        courses = obj.enrollment_set.all().order_by('course__name')
        serializer = EnrollmentStudentSerializer(courses, many=True)
        return serializer.data

    def get_tags(self, obj):
        tags = obj.tag_set.all().order_by('name')
        serializer = TagDetailSerializer(tags, many=True)
        return serializer.data

class CourseShallowSerializer(serializers.ModelSerializer):

    studentCount = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'name', 'image', 'recommendedYear', 'studentCount']
    
    def get_studentCount(self, obj):
        students = obj.enrollment_set.all().count()
        return students


class CourseDetailSerializer(serializers.ModelSerializer):

    students = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_students(self, obj):
        students = obj.enrollment_set.all().order_by('student__lastName')
        serializer = EnrollmentCourseSerializer(students, many=True)
        return serializer.data


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ['name']


class TagDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ['id','name']


class EnrollmentStudentSerializer(serializers.ModelSerializer):

    name = serializers.CharField(source="course.name")
    grades = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Enrollment
        fields = ['name','grades','id']

    def get_grades(self, obj):
        grades = obj.grade_set.all()
        serializer = GradeSerializer(grades, many=True)
        return serializer.data


class EnrollmentCourseSerializer(serializers.ModelSerializer):

    firstName = serializers.CharField(source="student.firstName")
    lastName = serializers.CharField(source="student.lastName")
    house = serializers.CharField(source="student.house")
    currentYear = serializers.IntegerField(source='student.currentYear')
    image = serializers.ImageField(source="student.image")

    grades = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Enrollment
        fields = ['firstName','lastName','grades','id','house','currentYear','image']

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