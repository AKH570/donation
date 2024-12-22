from django.urls import path
from zapp import views

urlpatterns=[
	path('',views.zhome,name='zhome'),
	path('donors/',views.Donor,name='donors'),
	path('donate/<int:pk>/',views.Donation,name='donate'),
	path('edit_donation/<int:pk>/',views.UpdateDonation,name='update_donation'),
	path('add_zrecipient/',views.AddZakatRecipients,name='add_zrecipient'),
	path('zakat_recipients/',views.ZakatRecipientsName,name='zakat_recipients'),
	path('zrecipients_update/<int:pk>/',views.EditZakatRecipients,name='zrecipients_update'),
	path('year23/',views.Zyear23,name='zyear23')
]