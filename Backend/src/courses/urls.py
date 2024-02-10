from django.urls import path
from .api import ListCreateCoursesApi,RetrieveUpdateDestroyCourse

urlpatterns = [
    path('',ListCreateCoursesApi.as_view()),
    path('edit_courses/<int:pk>/',RetrieveUpdateDestroyCourse.as_view()),
    
]
