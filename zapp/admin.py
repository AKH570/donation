from django.contrib import admin
from zapp.models import Donors,DonateInfo

# Register your models here.

@admin.register(Donors)
class DonorsModelAdmin(admin.ModelAdmin):
	list_display =['id','name','mobile_no']

@admin.register(DonateInfo)
class DonateInfoModelAdmin(admin.ModelAdmin):
	list_display=['id','d_name','donate_amt','sub_total','grand_total','zakat_year','donation_type','message','record_date','is_archived','created_at']