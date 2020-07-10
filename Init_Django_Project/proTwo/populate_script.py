import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proTwo.setting')

import django
django.setup()


##population script

import random
from appTwo.models import User
from faker import faker

fakegen = faker()

def populate(N = 6):
    for entry in range(N):

        fake_firstname = fakegen.first_name()
        fake_lastname  = fakegen.last_name()
        fake_email = fakegen.email()
        u = User.objects.get_or_create(first_name = fake_firstname, last_name = fake_lastname, email = fake_email)[0]


if __name__ == '__main__':
    print("Populating script")
    populate()
    print("Completed!")
