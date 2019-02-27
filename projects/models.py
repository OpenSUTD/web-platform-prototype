from django.db import models

# Mark out which fields cannot be empty
# (should raise an error if it's empty)

# Test that each model can be instantated, and updated to the database
# Test that models cannot be instantated without required fields

# Create your models here.
class Category (models.Model):
    name = models.CharField(max_length=30, default="None")

class Pillar(models.Model):
    name = models.CharField(max_length=4, default="None")

class Status(models.Model):
    # Approved, Rejected or Pending
    status = models.CharField(max_length=20, default="Not Approved")

class Tag(models.Model):
    name = models.CharField(max_length=30, default="None")

class User(models.Model):
    displayname = models.CharField(max_length=20, default="Tom")
    
    # probably a URL
    # (Use ImageField?)
    display_picture = models.CharField(max_length=200, default="https://via.placeholder.com/150")

    userid = models.CharField(max_length=200)

    isSUTD = models.BooleanField()

    graduationyear = models.IntegerField()

    pillar = models.ManyToManyField(Pillar)

    admin_groups = models.ManyToManyField(Category)

    contact_email = models.CharField(max_length=200, default="none@example.com")

    personal_links = models.CharField(max_length=200, default="")

    bio = models.CharField(max_length=300, default="")

class Project(models.Model):
    title = models.CharField(max_length=200, default="")

    # prefix + UID
    projectuid = models.CharField(max_length=20, default="NONE9999")

    # probably a URL
    # (Use ImageField?)
    featured_image = models.CharField(max_length=200, default="https://via.placeholder.com/150")

    owner = models.ManyToManyField(User)

    tags = models.ManyToManyField(Tag)

    caption = models.CharField(max_length=200)

    category = models.ManyToManyField(Category)

    # needs to be github url
    url = models.CharField(max_length=200)

    status = models.ManyToManyField(Status)

    published_date = models.DateTimeField(auto_now=True)
