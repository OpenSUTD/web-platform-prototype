import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'opensutd.settings')
sys.path.append('./')

import django

django.setup()

from projects.models import *

# create users

user_tom = User(user_id="tom",
                graduation_year=2020,
                pillar="ISTD")
user_tom.save()

user_jane = User(user_id="jane",
                graduation_year=2020,
                pillar="ISTD")
user_jane.save()

# get users from database

user_tom = User.objects.get(user_id="tom")
user_jane = User.objects.get(user_id="jane")

print("Retrieved users:")
print(user_tom, str(user_tom.user_id))
print(user_jane, str(user_jane.user_id))

project_1 = Project(title="OpenSUTD Web Platform 1",
                    project_uid="ACAD_00001",
                    caption="Sample project",
                    category="ACAD",
                    url="https://github.com/OpenSUTD/web-platform-prototype",
                    status="ACCEPT")

project_1.save()

project_1.users.add(user_tom)
project_1.users.add(user_jane)

project_1.save()

project_2 = Project(title="OpenSUTD Web Platform 2",
                    project_uid="ACAD_00002",
                    caption="Sample project",
                    category="ACAD",
                    url="https://github.com/OpenSUTD/web-platform-prototype",
                    status="ACCEPT")

project_2.save()

project_2.users.add(user_tom)
project_2.users.add(user_jane)

project_2.save()

print(User.objects.all())
print(Project.objects.all())