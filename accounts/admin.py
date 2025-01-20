from django.contrib import admin
from .models import UserAccount


class UserAccountAdmin(admin.ModelAdmin):
	list_display = ['user_name','email','is_active','is_admin','is_superuser','is_staff','date_created']
	list_filter=['is_active']
admin.site.register(UserAccount,UserAccountAdmin)

