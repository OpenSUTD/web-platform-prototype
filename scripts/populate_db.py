import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'opensutd.settings')

import django

django.setup()

from projects.models import *

print(Project.objects.all())