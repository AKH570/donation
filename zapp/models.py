from django.db import models
from django.utils.translation import gettext_lazy as _
import datetime

# Create your models here.

class Donors(models.Model):
	name = models.CharField(max_length=50,blank=True,null=True)
	mobile_no = models.CharField(max_length=20,blank=True,null=True)

	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural='DONORS'

class DonationType(models.TextChoices):
	select_type = '','-- Select --' 
	donation = 'donation','Donation'
	zakat = 'zakat','Zakat'
	others = 'other','Other_purpose'

YEAR_CHOICES = [(r, r) for r in range(2023, datetime.datetime.now().year + 1)]
# DONATION_TYPE = [
# 	('D','DONATION'),
# 	('Z','ZAKAT'),
# 	('O','OTHER PURPOSE')]
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