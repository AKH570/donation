from django.contrib import admin
from zapp.models import Donors,DonateInfo,ZakatRecipients,RecipientsArchive
from simple_history.admin import SimpleHistoryAdmin
# Register your models here.

@admin.register(Donors)
class DonorsModelAdmin(admin.ModelAdmin):
	list_display =['name','mobile_no']

@admin.register(DonateInfo)
class DonateInfoModelAdmin(admin.ModelAdmin):
	list_display=['d_name','donate_amt',
	'donation_type','message',
	'record_date']

@admin.register(ZakatRecipients)
class ZakatRecipientsAdmin(SimpleHistoryAdmin):
	list_display=['recipients_name','recipients_address',
	'recipients_mobile','zakat_money','donor_name','remarks',
	'recipients_category','zakat_year','donation_date',
	'created_at','updated_at','is_archived']

@admin.register(RecipientsArchive)
class RecipientsArchiveAdmin(admin.ModelAdmin):
	list_display=['recipients_name','recipients_address',
	'recipients_mobile','zakat_money','remarks','recipients_category',
	'zakat_year','donation_date','archive_date']