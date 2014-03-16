from django.contrib import admin

# Register your models here.
from django.contrib import admin
from myproject.myapp.models import *

#class UserAdmin(admin.ModelAdmin):
	#list_display = ('username', 'first_name', 'last_name', 'is_staff', 'is_active')

admin.site.register(Game)
admin.site.register(UserProfile)
