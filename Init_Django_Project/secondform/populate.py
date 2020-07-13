import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'secondform.settings')

import django
django.setup()

from theform.models import People
from faker import Faker

gen = Faker()

def populate(num = 10):
    for each in range(num):

        fake_first = gen.first_name()
        fake_last = gen.last_name()
        fake_email = gen.email()

        p = People.objects.get_or_create(first_name = fake_first,
                                        last_name = fake_last,
                                        email = fake_email)

if __name__ == "__main__":
    print("POPULATING...")
    populate(20)
    print('DONE...')
