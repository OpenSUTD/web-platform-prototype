from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Project)
admin.site.register(User)

admin.site.register(Pillar)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Status)