from django.contrib import admin
from .models import User

class UserProfileAdmin(admin.ModelAdmin):
    profilefields = ['nickname','profile_image','background_image','rank_point']

admin.site.register(User, UserProfileAdmin)
    


