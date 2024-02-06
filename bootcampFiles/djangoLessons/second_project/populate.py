import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'second_project.settings')

import django
django.setup()

# FAKE POP SCRIPT
import random
from second_app.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        # Create the fake data for that entry
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email = fakegen.email()

        # Create the new User entry
        user = User.objects.get_or_create(firstName=fake_first_name, lastName=fake_last_name, email=fake_email)[0]
        print(user)

if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    print("--------------------------")
    populate(20)
    print("--------------------------")
    print("Populating Complete")