from django.contrib import admin

from .models import Student, Course, Enrollment, Grade, Tag

# Register your models here.

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Grade)
admin.site.register(Tag)