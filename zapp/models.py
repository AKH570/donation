from django.db import models
from django.utils.translation import gettext_lazy as _
import datetime

# Create your models here.

class Donors(models.Model):
	name = models.CharField(max_length=200,blank=True,null=True)
	mobile_no = models.CharField(max_length=20,blank=True,null=True)

	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural='DONORS'

class DonationType(models.TextChoices): #choice fields
	select_type = '','-- Select --' 
	donation = 'donation','Donation'
	zakat = 'zakat','Zakat'
	others = 'other','Other_purpose'

YEAR_CHOICES = [(r, r) for r in range(2023, datetime.datetime.now().year + 1)]

class DonateInfo(models.Model):
	d_name = models.ForeignKey(Donors,on_delete=models.CASCADE,related_name='giver')
	donate_amt = models.DecimalField(max_digits=10,decimal_places=2,default=0)
	sub_total = models.DecimalField(max_digits=10,decimal_places=2,default=0,null=True,blank=True)
	grand_total = models.DecimalField(max_digits=10,decimal_places=2,default=0,null=True,blank=True)
	zakat_year = models.IntegerField(_('year'),choices=YEAR_CHOICES,default=datetime.datetime.now().year)
	message = models.CharField(max_length=200,null=True,blank=True)
	donation_type = models.CharField(max_length=50,null=True,choices=DonationType.choices)
	record_date = models.DateTimeField(null=True,blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	is_archived = models.BooleanField(default=False)
	
	def __str__(self):
		return self.d_name.name
	class Meta:
		verbose_name_plural='DONATE INFO'

RECIPIENTS_CAT=(
	('general','GENERAL'),
	('special','SPECIAL'),
	
)
class ZakatRecipients(models.Model): # NAME LIST
	recipients_name = models.CharField(max_length=150,blank=True,null=False)
	recipients_address = models.CharField(max_length=200,blank=True,null=True)
	zakat_money = models.DecimalField(max_digits=8,decimal_places=2,default=0)
	recipients_mobile = models.CharField(max_length=20,blank=True,null=True)
	donor_name = models.ForeignKey(Donors,on_delete=models.CASCADE,blank=True,null=True)
	remarks = models.CharField(max_length=100,blank=True,null=True)
	recipients_category =models.CharField(max_length=50,choices=RECIPIENTS_CAT,default='general')
	zakat_year = models.IntegerField(_('year'),choices=YEAR_CHOICES,default=datetime.datetime.now().year)
	donation_date =models.DateField(null=True,blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	is_archived = models.BooleanField(default=False)

	def __str__(self):
		return self.recipients_name

	class Meta:
		verbose_name_plural='ZAKAT RECIPIENTS'

	# def donor_list(self):
	# 	return ', '.join([donor.name for donor in self.donor_name.all()])
	# 	donor_list.short_description = 'Donors'

# ============ **** Archive Table ****==========

class RecipientsArchive(models.Model):
	recipients_name = models.CharField(max_length=150,blank=True,null=False)
	recipients_address = models.CharField(max_length=200,blank=True,null=True)
	zakat_money = models.DecimalField(max_digits=8,decimal_places=2,default=0)
	recipients_mobile = models.CharField(max_length=20,blank=True,null=True)
	remarks = models.CharField(max_length=100,blank=True,null=True)
	recipients_category =models.CharField(max_length=50)
	zakat_year = models.IntegerField()
	donation_date =models.DateField(null=True,blank=True) 
	archive_date = models.DateTimeField(auto_now_add=True) #his attribute sets the field to the current date only when the object is created.
	updated_at = models.DateTimeField(auto_now=True) # for update
	

	def __str__(self):
		return self.recipients_name