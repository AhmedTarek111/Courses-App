import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projet.settings')
django.setup()
from django.contrib.auth.models import User
from courses.models import Courses, Categories
from faker import Faker

fake = Faker()
categories = Categories.objects.all()

def seed_courses(n: int):
    for _ in range(n):  # Iterate using range(n)
        Courses.objects.create(
            user=User.objects.get(username='admin'),
            name=fake.name(),
            subtitle=fake.sentence(),
            description=fake.text(max_nb_chars=50),
            price=fake.random_int(min=100, max=500),
            category=fake.random.choice(categories)
        )

    print(f"Added products successfully")

seed_courses(5)
