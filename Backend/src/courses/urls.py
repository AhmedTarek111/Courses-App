from django.urls import path
from .api import ListCoursesApi

urlpatterns = [
    path('',ListCoursesApi.as_view())
]
