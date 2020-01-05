from django.contrib import admin

from profiles__api import models

# Register your models here.
admin.site.register(models.UserProfile)