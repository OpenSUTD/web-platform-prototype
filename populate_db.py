import csv
import django
import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'opensutd.settings')
sys.path.append('./')

django.setup()

from projects.models import *

# create superuser

um = OpenSUTDUserManager()

um.create_superuser("superadmin", password="asdf1234", display_name="",
                    graduation_year=0, pillar="", personal_links="", admin_groups=[])

# create users

um.create_user("tom", display_name="Tom Magnanti",
               display_picture="https://via.placeholder.com/150",
               graduation_year=2019, pillar="EPD")

um.create_user("jane", display_name="Jane Tan",
               display_picture="https://via.placeholder.com/150",
               graduation_year=2020, pillar="ESD")

um.create_user("harry", display_name="Harry Potter",
               display_picture="https://via.placeholder.com/150",
               graduation_year=2021, pillar="EPD")

um.create_user("shungit", display_name="Shun Git",
               display_picture="https://via.placeholder.com/150",
               graduation_year=2018, pillar="ISTD")

"""
um.create_user("tlkh", display_name="Timothy Liu",
               display_picture="https://via.placeholder.com/150",
               graduation_year=2020, pillar="ISTD")
"""

um.create_user("bob", display_name="Bob David",
               display_picture="https://via.placeholder.com/150",
               graduation_year=2019, pillar="ASD")

um.create_user("sikai", display_name="Ning Si Kai",
               display_picture="https://via.placeholder.com/150",
               graduation_year=2020, pillar="ISTD")

um.create_user("benghaun", display_name="Ang Beng Haun",
               display_picture="https://via.placeholder.com/150",
               graduation_year=2019, pillar="ISTD")

# retrieve those users from database

user_tom = User.objects.get(username="tom")
user_jane = User.objects.get(username="jane")
user_harry = User.objects.get(username="harry")
user_shungit = User.objects.get(username="shungit")
#user_timothy = User.objects.get(username="tlkh")
user_bob = User.objects.get(username="bob")
user_sikai = User.objects.get(username="sikai")
user_benghaun = User.objects.get(username="benghaun")

pm = OpenSUTDProjectManager()

with open("demo_data.csv") as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)
    for row in reader:
        [project_uid, title, caption, category, url, status, users, tags] = row
        print(row)

        pm.create_project(project_uid=project_uid,
                          title=title,
                          caption=caption,
                          category=category,
                          url=url)

        for user in users.split(","):
            print(user)
            pm.add_user_to_project(project_uid, user)

        pm.add_tag_to_project(project_uid, tags)

        pm.set_project_status(project_uid, status)


print(User.objects.all())
print(Project.objects.all())
