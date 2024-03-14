from rest_framework import serializers
from .models import Categories,Courses,Review
from django.db.models import Avg,Count

class CourseListSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    category=serializers.StringRelatedField()
    avgrate= serializers.SerializerMethodField()
    total_reviews= serializers.SerializerMethodField()
    
    

    def get_avgrate(self,obj):
        avg = obj.review_course.aggregate(rate_avg=Avg('rate'))
        rate_avg = avg['rate_avg']
        if rate_avg is not None:
            result = round(rate_avg, 1)
            return result
        else:
            return '0'
    def get_total_reviews(self,obj):
        total_reviews = obj.review_course.aggregate(reviews=Count('review'))
        reviews = total_reviews['reviews']
        return reviews
        
    class Meta():
        model =Courses
        fields = '__all__'
        
class CategoriesSerializer(serializers.ModelSerializer):
    class Meta():
        model =Categories
        fields ='__all__'

class ReviewSerializer(serializers.ModelSerializer):
    user= serializers.StringRelatedField()
    class Meta():
        model =Review
        fields ='__all__'

class CourseDetailSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    reviews = ReviewSerializer(source='review_course',many=True)
        
    class Meta():
        model =Courses
        fields = '__all__'