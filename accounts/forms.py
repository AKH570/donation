from django import forms
from .models import UserAccount

class UserForm(forms.ModelForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'input-md input-rounded form-control','maxlength':'100','placeholder':'Email'}))
	user_name = forms.CharField(widget=forms.TextInput(attrs={'class':'input-md input-rounded form-control','maxlength':'100','placeholder':'User Name'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input-md input-rounded form-control','maxlength':'100','placeholder':'Password'}))
	confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input-md input-rounded form-control','maxlength':'100','placeholder':'Confirm Password'}))
	class Meta:
		model = UserAccount
		fields = ['email','user_name','password']

		def clean(self):
			cleaned_data=super(UserForm,self).clean()
			password=cleaned_data.get('password')
			confirm_password=cleaned_data.get('confirm_password')

			if password != confirm_password:
				raise forms.ValidationError(
					'Password dose not matched'
				)