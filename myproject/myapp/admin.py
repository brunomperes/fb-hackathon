from django.contrib import admin
from myproject.myapp.models import *

# Register your models here.

#class UserAdmin(admin.ModelAdmin):
	#list_display = ('username', 'first_name', 'last_name', 'is_staff', 'is_active')

admin.site.register(Game)
admin.site.register(UserProfile)
