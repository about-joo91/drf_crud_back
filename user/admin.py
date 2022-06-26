from django.contrib import admin
from .models import Hobby, UserProfile, UserModel
# Register your models here.
admin.site.register(Hobby)
admin.site.register(UserProfile)
admin.site.register(UserModel)