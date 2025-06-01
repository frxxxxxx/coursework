import os
import django
import random
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myblog.settings')
django.setup()

from django.contrib.auth.models import User
from blog.models import Post

fake = Faker('ru_RU')

def run():
    for _ in range(20):
        username = fake.user_name()
        email = fake.email()
        password = '12345678'

        user = User.objects.create_user(username=username, email=email, password=password)
        Post.objects.create(
            author=user,
            title=fake.sentence(nb_words=5),
            content=fake.paragraph(nb_sentences=7)
        )

if __name__ == '__main__':
    run()
