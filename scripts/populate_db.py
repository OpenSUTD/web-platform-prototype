import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'opensutd.settings')
sys.path.append('./')

import django

django.setup()

from projects.models import *

# create users

user_tom = User(user_id="tom",
                display_name="Tom Magnanti",
                graduation_year=2020,
                pillar="ISTD")
user_tom.save()

user_jane = User(user_id="jane",
                display_name="Jane Tan",
                graduation_year=2020,
                pillar="ESD")
user_jane.save()

user_harry = User(user_id="harry",
                display_name="Harry Potter",
                graduation_year=2021,
                pillar="EPD")
user_harry.save()

# get users from database

user_tom = User.objects.get(user_id="tom")
user_jane = User.objects.get(user_id="jane")
user_harry = User.objects.get(user_id="harry")

print("Retrieved users:")
print(user_tom, str(user_tom.user_id))
print(user_jane, str(user_jane.user_id))

project_1 = Project(title="OpenSUTD Web Platform",
                    project_uid="ACAD_00001",
                    caption="Sample project 1",
                    category="ACAD",
                    url="https://github.com/OpenSUTD/web-platform-prototype",
                    status="ACCEPT")

project_1.save()

project_1.users.add(user_tom)
project_1.users.add(user_jane)

project_1.save()

project_2 = Project(title="Random Project 1",
                    project_uid="ACAD_00002",
                    caption="Sample project 2",
                    category="ACAD",
                    url="https://github.com/OpenSUTD/web-platform-prototype",
                    status="ACCEPT")

project_2.save()

project_2.users.add(user_jane)

project_2.save()

project_3 = Project(title="Random Project 2",
                    project_uid="ACAD_00003",
                    caption="Sample project 3",
                    category="ACAD",
                    url="https://github.com/OpenSUTD/web-platform-prototype",
                    status="ACCEPT")

project_3.save()

project_3.users.add(user_tom)
project_3.users.add(user_harry)

project_3.save()

print(User.objects.all())
print(Project.objects.all())