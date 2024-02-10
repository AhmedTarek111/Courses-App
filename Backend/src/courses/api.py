from .serializers import CourseListSerializer,CourseDetailSerializer,ReviewSerializer,CategoriesSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import Courses,Categories,Review
from rest_framework import filters


class ListCreateCoursesApi(ListCreateAPIView):
    model = Courses
    queryset = Courses.objects.all()
    serializer_class = CourseListSerializer
    filter_backends = [filters.SearchFilter,DjangoFilterBackend,filters.OrderingFilter]
    search_fields = [ 'name','subtitle','description']
    

class RetrieveUpdateDestroyCourse(RetrieveUpdateDestroyAPIView):
    queryset = Courses.objects.all()
    model = Courses
    serializer_class = CourseDetailSerializer

class ListCreateCategoriesApi(ListCreateAPIView):
    queryset=Categories.objects.all()
    model = Categories
    serializer_class = CategoriesSerializer
    
    