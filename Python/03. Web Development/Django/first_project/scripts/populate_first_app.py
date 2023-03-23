import os
import django
import random
from faker import Faker
from first_app.models import AccessRecord, Webpage, Topic

os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_projects.settings')
django.setup()

### Fake population script


def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']
 
