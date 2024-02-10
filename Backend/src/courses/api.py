from .serializers import CourseListSerializer,CourseDetailSerializer,ReviewSerializer,CategoriesSerializer
from rest_framework.generics import ListCreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import Courses,Categories,Review
from rest_framework import filters
import django_filters.rest_framework
from django.contrib.auth.models import User

class ListCreateCoursesApi(ListCreateAPIView):
    model = Courses
    queryset = Courses.objects.all()
    serializer_class = CourseListSerializer
    filter_backends = [filters.SearchFilter,DjangoFilterBackend,filters.OrderingFilter]
    search_fields = [ 'name','subtitle','description']