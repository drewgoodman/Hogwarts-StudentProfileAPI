from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

HOGWARTS_HOUSES = (
    (GRYFF:= 'GRYFFINDOR', "Gryffindor"),
    (RAVEN:= 'RAVENCLAW', "Ravenclaw"),
    (HUFFL:= 'HUFFLEPUFF', "Hufflepuff"),
    (SLYTH:= 'SLYTHERIN', "Slytherin"),
)

class Student(models.Model):

    id = models.AutoField(primary_key=True, editable=False)
    firstName = models.CharField(max_length=30, null=False, blank=True)
    lastName = models.CharField(max_length=30, null=False, blank=True)
    skill = models.CharField(max_length=50, null=True, blank=True)
    house = models.CharField(null=True, blank=True, max_length=10, choices=HOGWARTS_HOUSES, default=GRYFF)
    currentYear = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(7), MinValueValidator(1)])
    enrollDate = models.DateField(auto_now=False, auto_now_add=False)
    image = models.ImageField(
        upload_to="uploads/students/",
        null=True, blank=True,
        width_field="width_field",
        height_field="height_field"
    )
    height_field = models.IntegerField(default=0, null=True, blank=True)
    width_field = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.firstName


class Course(models.Model):

    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=30, null=False, blank=True)
    recommendedYear = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(7)])
    image = models.ImageField(
        upload_to="uploads/courses/",
        null=True, blank=True,
        width_field="width_field",
        height_field="height_field"
    )
    height_field = models.IntegerField(default=0, null=True, blank=True)
    width_field = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.name

class Enrollment(models.Model):

    id = models.AutoField(primary_key=True, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.student} in {self.course}'

    def course_name(self):
        return self.course.name

class Grade(models.Model):

    id = models.AutoField(primary_key=True, editable=False)
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    grade = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    date = models.DateField(auto_now=True)


class Tag(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=30)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)