from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Courses(models.Model):
    user=models.ForeignKey(User,related_name='course_user',on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    category= models.ForeignKey('Categories', models.SET_NULL,blank=True, null=True)
    
    def __str__(self) :
        return self.name
    
class Review(models.Model):
    user = models.ForeignKey(User,related_name='review_user',on_delete=models.SET_NULL,null=True)
    course = models.ForeignKey(Courses,related_name='review_course',on_delete=models.CASCADE)
    review = models.TextField(max_length=500)
    created_at = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self) :
        return self.review


class Categories(models.Model):
    name=models.CharField(max_length=50)
    
    
    def __str__(self) :
        return self.name