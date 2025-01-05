from django.contrib import admin
from zapp.models import Donors,DonateInfo,ZakatRecipients,RecipientsArchive

# Register your models here.

@admin.register(Donors)
class DonorsModelAdmin(admin.ModelAdmin):
	list_display =['id','name','mobile_no']

@admin.register(DonateInfo)
class DonateInfoModelAdmin(admin.ModelAdmin):
	list_display=['id','d_name','donate_amt','sub_total',
	'grand_total','zakat_year','donation_type','message',
	'record_date','is_archived','created_at']

@admin.register(ZakatRecipients)
class ZakatRecipientsAdmin(admin.ModelAdmin):
	list_display=['recipients_name','recipients_address',
	'recipients_mobile','zakat_money','donor_name','remarks',
	'recipients_category','zakat_year','donation_date','is_archived']

@admin.register(RecipientsArchive)
class RecipientsArchiveAdmin(admin.ModelAdmin):
	list_display=['recipients_name','recipients_address',
	'recipients_mobile','zakat_money','remarks','recipients_category',
	'zakat_year','donation_date','archive_date']