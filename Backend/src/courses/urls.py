from django.urls import path
from .api import ListCreateCoursesApi

urlpatterns = [
    path('',ListCreateCoursesApi.as_view()),
    
]
