from django.urls import path
from accounts import views

urlpatterns = [
		path('signup/',views.user_signup,name='signup'),
		path('login/',views.login_user,name='login'),
		path('logout/',views.user_logout,name='logout'),
]