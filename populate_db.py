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

project_1 = Project(title="OpenSUTD Web Platform",
                    project_uid="ACAD_00001",
                    caption="Sample project 1",
                    category="ACAD",
                    url="https://github.com/OpenSUTD/web-platform-prototype",
                    status="ACCEPT")

project_1.save()

project_1.users.add(user_tom)
project_1.users.add(user_jane)
#project_1.users.add(user_timothy)

project_1.tags.add("50.003", "Hello", "World", "OpenSUTD", "extremely long tag")

project_1.save()

project_2 = Project(title="Random Project 1",
                    project_uid="ACAD_00002",
                    caption="A random project to better the world by design",
                    category="ACAD",
                    url="https://github.com/OpenSUTD/web-platform-prototype",
                    status="ACCEPT")

project_2.save()

project_2.users.add(user_jane)

project_2.tags.add("Random", "World", "C")

project_2.save()

project_3 = Project(title="Random Project 2",
                    project_uid="ACAD_00003",
                    caption="Another random project to better the world by design",
                    category="ACAD",
                    url="https://github.com/OpenSUTD/web-platform-prototype",
                    status="PENDING")

project_3.save()

project_3.users.add(user_tom)
project_3.users.add(user_harry)

project_3.tags.add("Random", "Java", "IoT")

project_3.save()

project_4 = Project(title="SUTD Timetable",
                    project_uid="SELF_00001",
                    caption=".ics generator for SUTD Timetable",
                    category="SELF",
                    url="https://github.com/OpenSUTD/sutd-timetable",
                    status="ACCEPT")

project_4.save()

project_4.users.add(user_shungit)

project_4.save()

"""
project_5 = Project(title="SmartBin",
                    project_uid="ACAD_00004",
                    caption="1D Project: Spring 2018 10.009 Digital World",
                    category="ACAD",
                    url="https://github.com/OpenSUTD/SmartBin",
                    status="ACCEPT")

project_5.save()

project_5.users.add(user_timothy)

project_5.save()
"""

project_6 = Project(title="Project With Missing Info",
                    project_uid="UROP_00001",
                    caption="A third project to better the world by design; missing info; do not display!",
                    category="UROP",
                    url="https://github.com/OpenSUTD/web-platform-prototype",
                    status="PENDING")

project_6.save()

project_6.users.add(user_bob)
project_6.users.add(user_jane)

project_6.save()

project_7 = Project(title="ColourRun",
                    project_uid="ACAD_00005",
                    caption="50.002 Computational Structures Group 1-6 : Colour Run",
                    category="ACAD",
                    url="https://github.com/DoubleCapitals/CompStruct1D",
                    status="ACCEPT")

project_7.save()

project_7.users.add(user_sikai)

project_7.save()

project_8 = Project(title="SUTDtoSimei_bot",
                    project_uid="SELF_00002",
                    caption="Simple Telegram bot that checks bus timings to go to Simei from SUTD",
                    category="SELF",
                    url="https://github.com/benghaun/SUTDtoSimei_bot",
                    status="ACCEPT")

project_8.save()

project_8.users.add(user_benghaun)

project_8.save()

print(User.objects.all())
print(Project.objects.all())
