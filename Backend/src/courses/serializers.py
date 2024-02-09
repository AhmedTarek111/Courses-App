from rest_framework import serializers
from .models import Categories,Courses,Review

class CourseSerializer(serializers.ModelSerializer):
    class Meta():
        model =Courses
        fields = ['name','subtitle','description','price','category',]

class ReviewSerializer(serializers.ModelSerializer):
    class Meta():
        model =Review
        fields =['course','review']

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta():
        model =Categories
        fields =['name']