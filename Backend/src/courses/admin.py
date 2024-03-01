from django.contrib import admin
from .models import Courses, Review, Categories

class CoursesAdmin(admin.ModelAdmin):
    search_fields = ['name', 'description']
    list_display = ['name', 'price', 'category']  
    ordering = ['name', 'price'] 

    
admin.site.register(Courses, CoursesAdmin)
admin.site.register(Review)
admin.site.register(Categories)
