from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser,AbstractBaseUser,PermissionsMixin

# In summary, choose AbstractUser for projects that need standard user 
# functionality with minor modifications, while AbstractBaseUser is better suited for 
# applications requiring extensive customization of the user model and authentication logic.

class CustomUserManager(BaseUserManager):
	def create_user(self,user_name,email,password=None):
		if not email:
			raise ValueError("Users must have an email address")
		user = self.model(
			user_name=user_name,
			email=self.normalize_email(email),
			)
		user.set_password(password)
		user.save(using=self._db)
		return user	
	def create_superuser(self, user_name,email,password=None):
		user = self.create_user(
		user_name=user_name,
		email=self.normalize_email(email),
		password=password,
		)
		user.is_admin = True
		user.is_active= True
		user.is_superuser=True
		user.is_staff= True
		user.save(using=self._db)
		return user

# Inherit from PermissionsMixin in addition to 
# AbstractBaseUser. This provides fields and methods for
#  handling permissions and groups.
class UserAccount(AbstractBaseUser,PermissionsMixin):
	email = models.EmailField(max_length=100,unique=True)
	user_name = models.CharField(max_length=200)
	is_active = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	date_created = models.DateTimeField(auto_now_add=True)
	
	objects = CustomUserManager()
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['user_name']

	def __str__(self):
		return self.email
	def has_perm(self, perm, obj=None):
		return self.is_admin
	def has_module_perms(self, app_label):
		return True
	class Meta:
		verbose_name = 'User Account'
		verbose_name_plural = 'User Accounts'
		ordering = ['date_created']