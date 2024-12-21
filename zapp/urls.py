from django.urls import path
from zapp import views

urlpatterns=[
	path('',views.zhome,name='zhome'),
	path('donors/',views.Donor,name='donors'),
	path('donate/<int:pk>/',views.Donation,name='donate'),
	path('edit_donation/<int:pk>/',views.UpdateDonation,name='update_donation'),
	path('year23/',views.Zyear23,name='zyear23')
]