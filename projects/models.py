from django.db import models

# Mark out which fields cannot be empty
# (should raise an error if it's empty)

# Test that each model can be instantated, and updated to the database
# Test that models cannot be instantated without required fields

# Create your models here.
class Category (models.Model):
    pass

class Links(models.Model):
    pass

class AdminGroup(models.Model):
    pass

class Pillar(models.Model):
    pillar = models.CharField(max_length=10)

class Status(models.Model):
    # Approved, Rejected or Pending
    status = models.CharField(max_length=20)

class Tag(models.Model):
    pass

class User(models.Model):
    displayname = models.CharField(max_length=20)
    
    # probably a URL
    # (Use ImageField?)
    displaypicture = models.CharField(max_length=200)

    userid = models.CharField(max_length=200)

    issutd = models.BooleanField()

    graduationyear = models.IntegerField()

    pillar = models.ManyToManyField(Pillar)

    admingroup = models.ManyToManyField(AdminGroup)

    contactemail = models.CharField(max_length=200)

    personallinks = models.ManyToManyField(Links)

    bio = models.CharField(max_length=300)

class Project(models.Model):
    title = models.CharField(max_length=200)

    # prefix + UID
    projectuid = models.CharField(max_length=20)

    # probably a URL
    # (Use ImageField?)
    featuredimage = models.CharField(max_length=200)

    owner = models.ManyToManyField(User)

    tags = models.ManyToManyField(Tag)

    caption = models.CharField(max_length=200)

    category = models.ManyToManyField(Category)

    # needs to be github url
    url = models.CharField(max_length=200)

    status = models.ManyToManyField(Status)

class Tester(models.Model):
    projectuid = models.CharField(max_length=20)