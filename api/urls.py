from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name="api-overview"),
    path('students/', views.student_list, name="student-list"),
    # path('students/<str:pk', views.student_detail, name="student-detail"),
    path('courses/', views.courses_list, name="course-list")
]