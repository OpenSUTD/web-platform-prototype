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

with open("demo_user_data.csv") as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)
    for row in reader:
        [user_id, display_name, display_picture, graduation_year, pillar] = row
        print(row)

        um.create_user(user_id.lower().strip(), display_name=display_name.strip(),
                       display_picture=display_picture.strip(),
                       graduation_year=graduation_year,
                       pillar=pillar)

pm = OpenSUTDProjectManager()

with open("demo_project_data.csv") as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)
    for row in reader:
        [project_uid, title, caption, category, url, status, users, tags, featured_image] = row
        print(row)

        pm.create_project(project_uid=project_uid,
                          title=title,
                          caption=caption,
                          category=category,
                          url=url,
                          featured_image=featured_image)

        for user in users.split(","):
            print(user)
            pm.add_user_to_project(project_uid, user)

        pm.add_tag_to_project(project_uid, tags)

        pm.set_project_status(project_uid, status)

        pm.set_featured_image(project_uid, featured_image)


print(User.objects.all())
print(Project.objects.all())
