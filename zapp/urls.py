from django.urls import path
from zapp import views

urlpatterns=[
	path('',views.zhome,name='zhome'),
	path('donors/',views.Donor,name='donors'),
	path('donate/<int:pk>/',views.Donation,name='donate'),
	path('edit_donation/<int:pk>/',views.UpdateDonation,name='update_donation'),
	path('add_zrecipient/',views.AddZakatRecipients,name='add_zrecipient'),
	path('zakat_recipients/',views.ZakatRecipientsName,name='zakat_recipients'),
	# path('select_zrecipients/<slug:recipients_cat>/',views.FilterRecipients,name='select_zrecipients'),
	path('zrecipients_update/<int:pk>/',views.EditZakatRecipients,name='zrecipients_update'),
	path('remove_zrecipient/<int:pk>/',views.RemoveZakatRecipients,name='remove_zrecipient'),
	path('year_23/',views.recipients_23,name='year_23'),
	path('year_24/',views.recipients_24,name='year_24'),
]