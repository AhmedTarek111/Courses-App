from django.urls import path
from .api import ListCreateCoursesApi,RetrieveUpdateDestroyCourse,ListCreateCategoriesApi,CategoryFilterApi

urlpatterns = [
    path('',ListCreateCoursesApi.as_view()),
    path('edit_courses/<int:pk>/',RetrieveUpdateDestroyCourse.as_view()),
    path('categories/',ListCreateCategoriesApi.as_view()),
    path('filtercategories/<int:pk>/',CategoryFilterApi.as_view())
    
]
