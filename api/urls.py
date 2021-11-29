from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name="api-overview"),
    path('students/', views.student_list, name="student-list"),
    path('students/<str:pk>', views.student_detail, name="student-detail"),
    path('courses/', views.courses_list, name="course-list"),
    path('tags/', views.tags_list, name="tags-list"),
    path('tags/add', views.create_tag, name="create-tag"),
    path('tags/delete/<str:pk>', views.delete_tag, name='delete-tag')
]