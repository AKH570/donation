from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserAccount


class UserAccountAdmin(admin.ModelAdmin):
	list_display = ['email','user_name','is_active','is_admin','is_superuser','date_created']
	list_filter=()
admin.site.register(UserAccount,UserAccountAdmin)

