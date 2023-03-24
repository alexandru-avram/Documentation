import os
import django
import random
from faker import Faker
from first_app.models import AccessRecord, Webpage, Topic

# Setting up and configuring the porject settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_projects.settings')
django.setup()

### Fake population script

# Function to add topics
# get_or_create will retreive or create topics in our model
def add_topic():
    #[0] will be used since this will create a tuple, and we want to grab the frist item
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0] 
    t.save()
    return t

# Create an instance of the Faker object
fakegen = Faker()

# Createing a number of topics instances for our model
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']
 

def populate(N=5):
    for entry in range(N):
        
        # get the topic for the entry
        top = add_topic()
        
        # create the fake date for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        
        # create the new webapge entry
        webpg = Webpage.objects.get_or_create(topic = top, url = fake_url, name = fake_name)[0]
        
        # create a fake access record for that webpage
        acc_rec = AccessRecord.objects.get_or_create(name = webpg, date=fake_date)[0]
        
if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("populating complete!")