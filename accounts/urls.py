from django.urls import path
from accounts import views

urlpatterns=[
		path('signup/',views.user_signup,name='signup'),
		path('login/',views.LoginUser,name='login'),
		path('logout/',views.UserLogout,name='logout'),
	
]