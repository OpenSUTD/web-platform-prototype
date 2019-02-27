from django.db import models

# Mark out which fields cannot be empty
# (should raise an error if it's empty)

# Test that each model can be instantated, and updated to the database
# Test that models cannot be instantated without required fields

# Create your models here.

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

class Tag(models.Model):
    name = models.CharField(max_length=30, default="None", primary_key=True)

class User(models.Model):

    userid = models.CharField(max_length=200, primary_key=True)

    display_name = models.CharField(max_length=20, default="Tom")

    # TODO :
    # Eventually Move to ImageField instead of providing URL?
    display_picture = models.CharField(max_length=200, default="https://via.placeholder.com/150")

    isSUTD = models.BooleanField(default="False")

    graduation_year = models.IntegerField()

    pillar = models.CharField(max_length=4, choices=PILLAR_CHOICES, default="")

    admin_groups = models.CharField(max_length=4, choices=CATEGORY_CHOICES, default="")

    contact_email = models.CharField(max_length=200, default="none@example.com")

    personal_links = models.CharField(max_length=200, default="")

    bio = models.CharField(max_length=300, default="")

class Project(models.Model):
    title = models.CharField(max_length=200, default="")

    # this shall follow the format of CATEGORY_UID
    project_uid = models.CharField(max_length=20, default="NONE_9999", primary_key=True)

    # TODO :
    # Eventually Move to ImageField instead of providing URL?
    featured_image = models.CharField(max_length=200, default="https://via.placeholder.com/150")

    owner = models.ManyToManyField(User)

    tags = models.ManyToManyField(Tag)

    caption = models.CharField(max_length=200)

    category = models.CharField(max_length=4, choices=CATEGORY_CHOICES, default="NONE")

    # needs to be github url
    url = models.CharField(max_length=200)

    STATUS_CHOICES = (
        ("ACCEPT", "Accepted Project, will display"),
        ("REJECT", "Rejected Project, will not display"),
        ("PENDING", "Pending Project, will not display")
    )

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="PENDING")

    published_date = models.DateTimeField(auto_now=True)
