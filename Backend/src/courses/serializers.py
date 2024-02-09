from rest_framework import serializers
from .models import Categories,Courses,Review

class CourseListSerializer(serializers.ModelSerializer):
    class Meta():
        model =Courses
        fields = ['name','subtitle','description','price','category',]

class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta():
        model =Courses
        fields = ['name','category']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta():
        model =Review
        fields =['course','review']

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta():
        model =Categories
        fields =['name']