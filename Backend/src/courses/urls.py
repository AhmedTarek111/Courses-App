from django.urls import path
from .api import ListCreateCoursesApi,RetrieveUpdateDestroyCourse,ListCreateCategoriesApi,CategoryFilterApi,CreateReviewApi

urlpatterns = [
    path('',ListCreateCoursesApi.as_view()),
    path('edit_courses/<int:pk>/',RetrieveUpdateDestroyCourse.as_view()),
    path('categories/',ListCreateCategoriesApi.as_view()),
    path('categories/<int:pk>/',CategoryFilterApi.as_view()),
    path('create&delete/review/<int:pk>/',CreateReviewApi.as_view()),
    
]
