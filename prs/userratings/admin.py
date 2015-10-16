from django.contrib import admin

# Register your models here.
from userratings.models import Userprofile
from userratings.models import Userratings

admin.site.register(Userprofile)
admin.site.register(Userratings)