from django import forms
from zapp.models import DonateInfo,Donors,DonationType,ZakatRecipients

class DonorsNameForm(forms.ModelForm):
	name = forms.CharField(disabled=True,widget=forms.TextInput(attrs={'class':'input-md input-rounded form-control','maxlength':'100'}))
	mobile_no = forms.CharField(widget=forms.TextInput(attrs={'class':'input-md input-rounded form-control','maxlength':'100'}))
	class Meta:
		model=Donors
		fields = ['name','mobile_no']
		
class DonateInfoForm(forms.ModelForm):
	donate_amt = forms.CharField(widget=forms.TextInput(attrs={'class':'input-md input-rounded form-control','maxlength':'100','placeholder':'TK'}))
	message	= forms.CharField(widget=forms.TextInput(attrs={'class':'input-md input-rounded form-control','maxlength':'100','placeholder':'Remarks'}))
	donation_type = forms.ChoiceField(choices=DonationType.choices,label='',widget=forms.Select(attrs={'class':'input-md input-rounded form-control','maxlength':'50','placeholder':'Select Donation Type'}),initial=DonationType.select_type)#placeholder options
	record_date	= forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'datetime-local','class':'input-md input-rounded form-control','maxlength':'100'}))

	class Meta:
		model=DonateInfo
		fields = ['donate_amt','message','donation_type','record_date']

class ZakatRecipientsForm(forms.ModelForm):
	recipients_name = forms.CharField(widget=forms.TextInput(attrs={
		'class':'input-md input-rounded form-control',
		'maxlength':'150','placeholder':'Recipients Name'}),max_length=150)
	recipients_address	= forms.CharField(widget=forms.TextInput(attrs={
		'class':'input-md input-rounded form-control',
		'maxlength':'200','placeholder':'Address'}),required=False)
	zakat_money	= forms.DecimalField(widget=forms.TextInput(attrs={
		'class':'input-md input-rounded form-control',
		'maxlength':'8',
		'placeholder':'Amount'}),max_digits=8,decimal_places=2,required=True)
	recipients_mobile	= forms.CharField(widget=forms.TextInput(attrs={
		'class':'input-md input-rounded form-control',
		'maxlength':'11',
		'placeholder':'Mobile No'}),required=False)
	remarks	= forms.CharField(widget=forms.TextInput(attrs={
		'class':'input-md input-rounded form-control',
		'maxlength':'100',
		'placeholder':'Reference'}),required=False,max_length=100)
	recipients_category	= forms.ChoiceField(choices=ZakatRecipients._meta.get_field('recipients_category').choices,label='Category',widget=forms.Select(attrs={'class':'input-md input-rounded form-control'})) # The _meta API allows you to access various attributes of your model fields programmatically, including their choices.
	zakat_date	= forms.DateTimeField(widget=forms.DateTimeInput(attrs={
		'type':'datetime-local',
		'class':'input-md input-rounded form-control',
		'maxlength':'100'}))

	class Meta:
		model=ZakatRecipients
		fields = ['recipients_name',
		'recipients_address',
		'zakat_money',
		'recipients_mobile',
		'recipients_category',
		'remarks',
		'zakat_date']