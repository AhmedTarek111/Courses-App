from .serializers import CourseListSerializer,CourseDetailSerializer,ReviewSerializer,CategoriesSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import Courses,Categories,Review
from rest_framework import filters
from .myfilter import CoursesFilter
from .mypagination import CustomPagination

class ListCreateCoursesApi(ListCreateAPIView):
    model = Courses
    queryset = Courses.objects.all()
    serializer_class = CourseListSerializer
    filter_backends = [filters.SearchFilter,DjangoFilterBackend,filters.OrderingFilter]
    search_fields = [ 'name','subtitle','description']
    ordering_fields = ['name', 'price']
    filterset_class = CoursesFilter
    pagination_class= CustomPagination
    
class RetrieveUpdateDestroyCourse(RetrieveUpdateDestroyAPIView):
    model = Courses
    queryset = Courses.objects.all()
    serializer_class = CourseDetailSerializer

class ListCreateCategoriesApi(ListCreateAPIView):
    model = Categories
    queryset=Categories.objects.all()
    serializer_class = CategoriesSerializer