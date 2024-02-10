import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projet.settings')
django.setup()
from django.contrib.auth.models import User
from courses.models import Courses, Categories,Review
from faker import Faker

fake = Faker()
categories = Categories.objects.all()

def seed_courses(n: int):
    for _ in range(n): 
        Courses.objects.create(
            user=User.objects.get(username='admin'),
            name=fake.name(),
            subtitle=fake.sentence(),
            description=fake.text(max_nb_chars=50),
            price=fake.random_int(min=100, max=500),
            category=fake.random.choice(categories)
        )

    print(f"Added products successfully")

def seed_reviews(n:int):
    all_courses=list(Courses.objects.all())
    for _ in range(n):
        Review.objects.create(
            user=User.objects.get(username='admin'),
            review=fake.text(max_nb_chars=30),
            course=fake.random.choice(all_courses)
            
            


        )

seed_courses(100)
