from rest_framework import serializers
from .models import Categories,Courses,Review

class CourseListSerializer(serializers.ModelSerializer):
    category=serializers.StringRelatedField()
    class Meta():
        model =Courses
        fields = ['name','subtitle','description','price','category',]

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta():
        model =Categories
        fields =['name']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta():
        model =Review
        fields =['course','review','created_at']

class CourseDetailSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    reviews = ReviewSerializer(source='review_course',many=True)    
    class Meta():
        model =Courses
        fields = ['name','category','reviews']
