from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class Courses(models.Model):
    user=models.ForeignKey(User,related_name='course_user',on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    price = models.FloatField()
    category= models.ForeignKey('Categories', models.SET_NULL,blank=True, null=True)
    image=models.ImageField(upload_to='course_images/',default='default-course-img.jpeg')
   
    def __str__(self) :
        return self.name
    
class Review(models.Model):
    user = models.ForeignKey(User,related_name='review_user',on_delete=models.SET_NULL,null=True)
    course = models.ForeignKey(Courses,related_name='review_course',on_delete=models.CASCADE)
    review = models.TextField(max_length=500)
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(default=timezone.now)
    
    
   
    
    def __str__(self) :
        return self.review


class Categories(models.Model):
    name=models.CharField(max_length=50)
    
    def __str__(self) :
        return self.name