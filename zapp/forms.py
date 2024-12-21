from django import forms
from zapp.models import DonateInfo,Donors,DonationType

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