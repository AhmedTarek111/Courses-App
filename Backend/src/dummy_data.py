import os
import django
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
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
            category=fake.random.choice(categories),
            image = 'default-course-img.jpeg'
        )

    print(f"Added {n} products successfully")

def seed_reviews(n:int):
    all_courses=list(Courses.objects.all())
    for _ in range(n):
        Review.objects.create(
            user=User.objects.get(username='admin'),
            course=fake.random.choice(all_courses),
            review=fake.text(max_nb_chars=30),
            rate=random.randint(1, 5),
        )

    print(f"Added {n} reviews successfully")
seed_courses(98)
