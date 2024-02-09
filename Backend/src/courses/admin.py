from django.contrib import admin
from .models import Courses, Review, Categories

class CategoriesInline(admin.TabularInline):
    model = Categories
    extra = 1

class CoursesAdmin(admin.ModelAdmin):
    inlines = [CategoriesInline,]

admin.site.register(Courses)
admin.site.register(Review)
admin.site.register(Categories)
