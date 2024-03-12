from .serializers import CourseListSerializer,CourseDetailSerializer,ReviewSerializer,CategoriesSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,GenericAPIView,CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import Courses,Categories,Review
from rest_framework import filters
from .myfilter import CoursesFilter
from .mypagination import CustomPagination
from django.db.models import Q
from rest_framework.response import Response

class ListCreateCoursesApi(ListCreateAPIView):
    model = Courses
    queryset = Courses.objects.all()
    serializer_class = CourseListSerializer
    filter_backends = [filters.SearchFilter,DjangoFilterBackend,filters.OrderingFilter]
    search_fields = [ 'name','subtitle','description']
    ordering_fields = ['name', 'price']
    filterset_class = CoursesFilter
    pagination_class= CustomPagination
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('query', None)
        if search_query is not None:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(subtitle__icontains=search_query) |
                Q(description__icontains=search_query)
            )
        return queryset
    
class RetrieveUpdateDestroyCourse(RetrieveUpdateDestroyAPIView):
    model = Courses
    queryset = Courses.objects.all()
    serializer_class = CourseDetailSerializer

class ListCreateCategoriesApi(ListCreateAPIView):
    model = Categories
    queryset=Categories.objects.all()
    serializer_class = CategoriesSerializer
    
class CategoryFilterApi(GenericAPIView):
    serializer_class = CourseListSerializer
    queryset = Courses.objects.all()
    pagination_class= CustomPagination

    def get(self,request,*args, **kwargs):
        category = Categories.objects.get(id=self.kwargs['pk'])
        filterdcourses = Courses.objects.filter(category = category)
        serializer = self.get_serializer(filterdcourses, many=True)
        return Response(serializer.data)
    
class CreateReviewApi(GenericAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    
    def post(self,request,*args, **kwargs):
        course = Courses.objects.get(id=self.kwargs['pk'])
        review = Review.objects.create(
            user = request.user,
            course = course,
            rate = request.data.get('rate'),
            review =request.data.get('review')
        )
        
        serializer = self.get_serializer(review)
        return Response(serializer.data)
    
