from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.contrib.auth import hashers
from django.utils.translation import ugettext_lazy as _
from taggit.managers import TaggableManager
from taggit.models import CommonGenericTaggedItemBase, TaggedItemBase

import datetime
CURRENT_YEAR = datetime.datetime.now().year

# FIXED CHOICES DEFINITIONS
# The first element in each tuple is the value that will be stored in the database.
# The second element is displayed by the field’s form widget.

PILLAR_CHOICES = (
    ("FRSH", "Freshmore"),
    ("EPD", "Engineering Product and Design"),
    ("ESD", "Engineering Systems Design"),
    ("ASD", "Architecture and Sustainable Design"),
    ("ISTD", "Information Systems Technology and Design"),
    ("PSTG", "Post-graduate")
)

CATEGORY_CHOICES = (
    ("UROP", "Undergraduate Research Opportunities Project"),
    ("UTOP", "Undergraduate Teaching Opportunities Project"),
    ("ACAD", "Academic Project (1D, 2D etc.)"),
    ("SELF", "Student-initiated project"),
    ("NONE", "Unknown, or doesn't fall into any category")
)

STATUS_CHOICES = (
    ("ACCEPT", "Accepted Project, will display"),
    ("REJECT", "Rejected Project, will not display"),
    ("PENDING", "Pending Project, will not display")
)

# Mark out which fields cannot be empty
# (should raise an error if it's empty)

# Test that each model can be instantated, and updated to the database
# Test that models cannot be instantated without required fields

# Create your models here.


class User(AbstractUser):

    display_name = models.CharField(max_length=20, default="")

    # TODO :
    # Eventually Move to ImageField instead of providing URL?
    display_picture = models.CharField(
        max_length=200, default="http://pluspng.com/img-png/user-png-icon-male-user-icon-512.png")

    is_sutd = models.BooleanField(default="False")

    graduation_year = models.IntegerField(default=CURRENT_YEAR+3)

    pillar = models.CharField(max_length=4, choices=PILLAR_CHOICES, default="")

    admin_groups = models.CharField(
        max_length=4, choices=CATEGORY_CHOICES, default="")

    contact_email = models.CharField(
        max_length=200, default="none@example.com")

    personal_links = models.CharField(max_length=200, default="")

    bio = models.CharField(max_length=300, default="")


class GenericStringTaggedProject(CommonGenericTaggedItemBase, TaggedItemBase):
    object_id = models.CharField(
        max_length=50, verbose_name=_('Object id'), db_index=True)


class Project(models.Model):
    title = models.CharField(max_length=200, default="")

    # CATEGORY_PROJECTUID
    project_uid = models.CharField(max_length=20, default="", primary_key=True)

    # TODO :
    # Eventually Move to ImageField instead of providing URL?
    featured_image = models.CharField(
        max_length=200, default="https://via.placeholder.com/500x250?text=project_featured_image")

    users = models.ManyToManyField(User)

    caption = models.CharField(max_length=200)

    category = models.CharField(
        max_length=4, choices=CATEGORY_CHOICES, default="NONE")

    # needs to be github url
    url = models.CharField(max_length=200)

    poster_url = models.CharField(
        max_length=200, default="https://via.placeholder.com/900x400?text=project_poster_image")

    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="PENDING")

    published_date = models.DateTimeField(auto_now=True)

    tags = TaggableManager(through=GenericStringTaggedProject)

    def is_accepted(self):
        return self.status == "ACCEPT"


class OpenSUTDProjectManager(object):

    def create_project(self, project_uid, title, caption, category, url,
                       poster_url="", featured_image="",
                       users=None, status="PENDING"):

        # validation

        # TODO:
        # - validate github url

        project = Project(project_uid=project_uid,
                          title=title,
                          caption=caption,
                          category=category,
                          url=url,
                          poster_url=poster_url,
                          featured_image=featured_image,
                          status=status)

        project.save()

    def add_user_to_project(self, project_uid, user_id):
        project = Project.objects.get(project_uid=project_uid)
        user = User.objects.get(username=user_id)
        project.users.add(user)
        project.save()

    def add_tag_to_project(self, project_uid, tags):
        tags = tags.split(",")
        project = Project.objects.get(project_uid=project_uid)
        for tag in tags:
            tag = tag.lower().strip()
            project.tags.add(tag)

        project.save()

    def set_project_status(self, project_uid, status):
        project = Project.objects.get(project_uid=project_uid)
        project.status = status

        project.save()
    
    def set_featured_image(self, project_uid, featured_image):
        project = Project.objects.get(project_uid=project_uid)
        project.featured_image = featured_image

        project.save()


class OpenSUTDUserManager(BaseUserManager):

    def create_user(self, user_id, display_name="",
                    display_picture="https://via.placeholder.com/150",
                    graduation_year=0, pillar="",
                    personal_links="", admin_groups=[], password="password1"):

        if display_name == "":
            display_name = user_id

        # https://docs.djangoproject.com/en/2.1/topics/auth/passwords/#module-django.contrib.auth.hashers
        password = hashers.make_password(password)

        user = User(username=user_id,
                    display_name=display_name,
                    graduation_year=graduation_year,
                    pillar=pillar,
                    personal_links=personal_links,
                    admin_groups=admin_groups,
                    password=password)

        user.save()

    def create_superuser(self, user_id, password, display_name="", graduation_year=0, pillar="", personal_links="", admin_groups=[]):

        if display_name == "":
            display_name = user_id

        password = hashers.make_password(password)

        superuser = User(username=user_id,
                         display_name=display_name,
                         graduation_year=graduation_year,
                         pillar=pillar,
                         personal_links=personal_links,
                         admin_groups=admin_groups,
                         password=password,
                         is_staff=True,
                         is_superuser=True)

        superuser.save()
