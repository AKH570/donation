from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import login,authenticate
from accounts.forms import UserForm
from accounts.models import UserAccount
# Create your views here.

def user_signup(request):
	if request.method == 'POST':
		signup_form = UserForm(request.POST)
		if signup_form.is_valid():
			user_account = UserAccount()
			user_account.email = signup_form.cleaned_data['email']
			user_account.user_name = signup_form.cleaned_data['user_name']
			# user_account.password = signup_form.cleaned_data['password']
			user_account.set_password(signup_form.cleaned_data['password'])
			user_account.is_active = False
			user_account.save()
			messages.success(request,'Congratulations! You can not log in until your user is active.')
			return redirect('login')
		else:
			print(signup_form.errors)
	else:
		signup_form = UserForm()
	context = {
		'signup_form':signup_form
	}
	return render(request,'users/registration.html',context)

def login_user(request):
	if request.method =="POST":
		email = request.POST.get('email')
		password = request.POST.get('password')

		# The authenticate method typically uses username 
		# instead of email. If you want to authenticate users
		#  by email, ensure that your user model supports this. 
		user = authenticate(email=email,password=password)

		if user is not None :
			auth.login(request, user)
			return redirect('zhome')
		else:
			messages.error(request,'Invalid Email or Password')
			return render(request,'users/login.html')

	return render(request,'users/login.html')

def user_logout(request):
	auth.logout(request)
	return redirect('zhome')
