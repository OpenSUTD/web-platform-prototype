from django.db import models

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

class Tag(models.Model):
    name = models.CharField(max_length=40, default="")

class User(models.Model):

    user_id = models.CharField(max_length=200, primary_key=True)

    display_name = models.CharField(max_length=20, default="")

    # TODO :
    # Eventually Move to ImageField instead of providing URL?
    display_picture = models.CharField(max_length=200, default="https://via.placeholder.com/150")

    is_sutd = models.BooleanField(default="False")

    graduation_year = models.IntegerField()

    pillar = models.CharField(max_length=4, choices=PILLAR_CHOICES, default="")

    admin_groups = models.CharField(max_length=4, choices=CATEGORY_CHOICES, default="")

    contact_email = models.CharField(max_length=200, default="none@example.com")

    personal_links = models.CharField(max_length=200, default="")

    bio = models.CharField(max_length=300, default="")

class Project(models.Model):
    title = models.CharField(max_length=200, default="")

    # CATEGORY_PROJECTUID
    project_uid = models.CharField(max_length=20, default="", primary_key=True)

    # TODO :
    # Eventually Move to ImageField instead of providing URL?
    featured_image = models.CharField(max_length=200, default="https://via.placeholder.com/500x250?text=project_featured_image")

    users = models.ManyToManyField(User)

    tags = models.ManyToManyField(Tag)

    caption = models.CharField(max_length=200)

    category = models.CharField(max_length=4, choices=CATEGORY_CHOICES, default="NONE")

    # needs to be github url
    url = models.CharField(max_length=200)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="PENDING")

    published_date = models.DateTimeField(auto_now=True)
