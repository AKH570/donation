from django import forms
from zapp.models import DonateInfo,Donors,DonationType,ZakatRecipients
from django.contrib.auth.forms import AuthenticationForm



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
	record_date	= forms.DateField(widget=forms.DateInput(attrs={'type':'date','class':'input-md input-rounded form-control'}))

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
	recipients_category	= forms.ChoiceField(choices=ZakatRecipients._meta.get_field(
		'recipients_category').choices,label='Category',widget=forms.Select(attrs=
		{'class':'input-md input-rounded form-control'})) # The _meta API allows you to access various attributes of your model fields programmatically, including their choices.
	donation_date	= forms.DateField(widget=forms.DateInput(attrs={
		'type':'date',
		'class':'input-md input-rounded form-control'
		}))
	zakat_year	= forms.ChoiceField(choices=ZakatRecipients._meta.get_field('zakat_year').choices,widget=forms.Select(attrs={
		'class':'input-md input-rounded form-control'
		}))

	class Meta:
		model=ZakatRecipients
		fields = ['recipients_name',
		'recipients_address',
		'zakat_money',
		'recipients_mobile',
		'recipients_category',
		'remarks',
		'donation_date',
		'zakat_year']

# class LoginForm(AuthenticationForm):
#     username = forms.CharField(
#         widget=forms.TextInput(attrs={
# 		'class':'input-md input-rounded form-control',
# 		'maxlength':'150','placeholder':'User Name'}),
#         label='',
#         max_length=150,
#     )
#     password = forms.CharField(
#         widget=forms.PasswordInput(attrs={
# 		'class':'input-md input-rounded form-control',
# 		'maxlength':'150','placeholder':'Password'}),
#         label='',
#     )

