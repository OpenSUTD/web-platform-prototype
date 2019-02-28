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

user_shungit = User(user_id="shungit",
                display_name="Shun Git",
                graduation_year=2018,
                pillar="ISTD")
user_shungit.save()

user_timothy = User(user_id="tlkh",
                display_name="Timothy Liu",
                graduation_year=2020,
                pillar="ISTD")
user_timothy.save()

user_bob = User(user_id="bob",
                display_name="Bob Ross",
                graduation_year=2019,
                pillar="ASD")
user_bob.save()

user_sikai = User(user_id="sikai",
                display_name="Ning Si Kai",
                graduation_year=2020,
                pillar="ISTD")
user_sikai.save()

user_benghaun = User(user_id="benghaun",
                display_name="Ang Beng Haun",
                graduation_year=2019,
                pillar="ISTD")

user_benghaun.save()

# retrieve those users from database

user_tom = User.objects.get(user_id="tom")
user_jane = User.objects.get(user_id="jane")
user_harry = User.objects.get(user_id="harry")
user_shungit = User.objects.get(user_id="shungit")
user_timothy = User.objects.get(user_id="tlkh")
user_bob = User.objects.get(user_id="bob")
user_sikai = User.objects.get(user_id="sikai")
user_benghaun = User.objects.get(user_id="benghaun")

project_1 = Project(title="OpenSUTD Web Platform",
                    project_uid="ACAD_00001",
                    caption="Sample project 1",
                    category="ACAD",
                    url="https://github.com/OpenSUTD/web-platform-prototype",
                    status="ACCEPT")

project_1.save()

project_1.users.add(user_tom)
project_1.users.add(user_jane)
project_1.users.add(user_timothy)

project_1.save()

project_2 = Project(title="Random Project 1",
                    project_uid="ACAD_00002",
                    caption="A random project to better the world by design",
                    category="ACAD",
                    url="https://github.com/OpenSUTD/web-platform-prototype",
                    status="ACCEPT")

project_2.save()

project_2.users.add(user_jane)

project_2.save()

project_3 = Project(title="Random Project 2",
                    project_uid="ACAD_00003",
                    caption="Another random project to better the world by design",
                    category="ACAD",
                    url="https://github.com/OpenSUTD/web-platform-prototype",
                    status="ACCEPT")

project_3.save()

project_3.users.add(user_tom)
project_3.users.add(user_harry)

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

project_5 = Project(title="SmartBin",
                    project_uid="ACAD_00004",
                    caption="1D Project: Spring 2018 10.009 Digital World",
                    category="ACAD",
                    url="https://github.com/OpenSUTD/SmartBin",
                    status="ACCEPT")

project_5.save()

project_5.users.add(user_timothy)

project_5.save()

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