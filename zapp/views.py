from django.shortcuts import render,get_object_or_404,redirect
from zapp.models import Donors,DonateInfo,ZakatRecipients,RecipientsArchive
from zapp.forms import DonateInfoForm,DonorsNameForm,ZakatRecipientsForm
from django.db.models import Sum
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages,auth
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import user_passes_test,login_required
from accounts.models import UserAccount



	

# Create your views here.
def zhome(request):
	return render(request,'zakat/zhome.html')

def Donor(request):
	name = Donors.objects.all()
	donate_info = DonateInfo.objects.all()
	
	''' donor individual total amount /row wise total'''
	donors_info = Donors.objects.annotate(
        donors_subtotal=Sum('giver__donate_amt')
    )
	
	# count no of total recipients
	try:
		recipients_list = ZakatRecipients.objects.exclude(recipients_name__isnull=True)
		recipients_num =recipients_list.count()
	except ZakatRecipients.DoesNotExist:
		messages.warning(request,'No recipients found')

	total_donate_amount = 0
	for i in donate_info:
		total_donate_amount += i.donate_amt
	
	proposed_zakat_amount=0
	for i in recipients_list:
		proposed_zakat_amount += i.zakat_money
	context = {
		'dname':name,
		'donate_info':donate_info,
		'donors_info':donors_info,
		'total_donate_amount':total_donate_amount,
		'proposed_zakat_amount':proposed_zakat_amount,
		'recipients_num':recipients_num
	}
	return render(request,'zakat/zdonors.html',context) # old:zcontributors.html
# @login_required
def Donation(request,pk):
	name = get_object_or_404(Donors,id=pk)
	# print(f'name:{name}')
	if request.user.is_authenticated:
		if request.method=='POST':
			donate_inf_form = DonateInfoForm(request.POST)
			if donate_inf_form.is_valid():
				donate_info = DonateInfo()
				donate_info.d_name=name
				donate_info.donate_amt=donate_inf_form.cleaned_data['donate_amt']
				donate_info.record_date=donate_inf_form.cleaned_data['record_date']
				donate_info.message=donate_inf_form.cleaned_data['message']
				donate_info.donation_type=request.POST.get('donation_type')
				donate_info.save()
				messages.success(request,'Alhamdulillah! Your fund has been added.')
				return redirect('donors')
			else:
				print(donate_inf_form.errors)
		else:
			d_info_form = DonateInfoForm()
			donor_name_form = DonorsNameForm(instance=name)
	else:
		messages.warning(request,'Only admin user can perform this action')
		return redirect('donors')
	context={
		'dinfo_form':d_info_form,
		'donor_name':donor_name_form
	}

	return render(request,'zakat/donatemoney.html',context)

# @login_required
def UpdateDonation(request,pk):
	get_donation = get_object_or_404(DonateInfo,pk=pk)
	try:
		get_donor = Donors.objects.get(name=get_donation)
	except Donors.DoesNotExist:
		messages.error(request,'Donor is not exist')
		return redirect('donors')
	if request.user.is_authenticated:
		if request.method == 'POST':
			donation_form = DonateInfoForm(request.POST,instance=get_donation)
			if donation_form.is_valid():
				donation_form.save()
				messages.success(request,'Donation have been updated successfully')
				return redirect('donors')
			else:
				print(donation_form.errors)
				
		else:
			donor_form = DonorsNameForm(instance=get_donor)
			donation_form = DonateInfoForm(instance=get_donation)

	else:
		messages.warning(request,'Only admin user can perform this action')
		return redirect('donors')
	context={
		'dinfo_form':donation_form,
		'donor_name':donor_form
	}
	return render(request,'zakat/update_donation.html',context)
#-----------------end donation ---------------------
#----------------- donation receipients--------------

def AddZakatRecipients(request):
	if request.method=='POST':
		zakat_form = ZakatRecipientsForm(request.POST)
		if zakat_form.is_valid():
			zRecipients = ZakatRecipients()
			zRecipients.recipients_name = zakat_form.cleaned_data['recipients_name']
			zRecipients.recipients_address = zakat_form.cleaned_data['recipients_address']
			zRecipients.zakat_money = zakat_form.cleaned_data['zakat_money']
			zRecipients.recipients_mobile = zakat_form.cleaned_data['recipients_mobile']
			zRecipients.remarks = zakat_form.cleaned_data['remarks']
			zRecipients.recipients_category = request.POST.get('recipients_category')
			
			zRecipients.zakat_year = zakat_form.cleaned_data['zakat_year']
			zRecipients.donation_date = zakat_form.cleaned_data['donation_date']

			zRecipients.save()
			messages.success(request,'Recipients name added successfully')
			return redirect('add_zrecipient')
		else:
			print(zakat_form.errors)

	else:
		zakat_form = ZakatRecipientsForm()

	context={
		'zakat_form':zakat_form,
		
	}
	return render(request,'zakat/add_zakat_recipients.html',context)

# To show recipients list in template
def ZakatRecipientsName(request,recipients_num = None):
	recipients_list = ZakatRecipients.objects.all().order_by('created_at')

	# count total recipients:
	try:
		recipients_num = ZakatRecipients.objects.exclude(recipients_name__isnull=True).count()
	except ZakatRecipients.DoesNotExist:
		messages.warning(request,'No recipients found')

	# display total donation
	donation = DonateInfo.objects.all()
	total_donate_amount = 0
	for i in donation:
		total_donate_amount += i.donate_amt
	
	# display total proposed zakat amount
	proposed_zakat_amount=0
	for i in recipients_list:
		proposed_zakat_amount += i.zakat_money
	print(f'zakat money:{proposed_zakat_amount}')
	context={
		'recipients_list':recipients_list,
		'total_donate_amount':total_donate_amount,
		'proposed_zakat_amount':proposed_zakat_amount,
		'recipients_num':recipients_num
	}
	return render(request,'zakat/zakat_recipients.html',context)

# @login_required
def EditZakatRecipients(request,pk):
	get_zakat_recipient_name = get_object_or_404(ZakatRecipients,pk=pk)
	if request.user.is_authenticated:
		if request.method=='POST':
			zakat_form = ZakatRecipientsForm(request.POST,instance=get_zakat_recipient_name)
			if zakat_form.is_valid():
				zakat_recipient_instance = zakat_form.save(commit=False) # Save but don't commit yet
				zakat_recipient_instance._change_reason = f"Updated by {request.user}"  # Set change reason
				zakat_recipient_instance.save()
				messages.success(request,'Recipients updated successfully')
				return redirect('zakat_recipients')
			else:
				print(zakat_form.errors)
		else:
			zakat_form = ZakatRecipientsForm(instance=get_zakat_recipient_name)
	else:
		messages.warning(request,'Only Admin User Can Update')
		return redirect('zakat_recipients')
	context={
		'zakat_form':zakat_form
	}	
	return render(request,'zakat/update_zakat_recipt.html',context)

# @user_passes_test(lambda u: u.is_superuser)
def RemoveZakatRecipients(request,pk):
	if request.user.is_authenticated:
		try:
			delete_zrecipient = ZakatRecipients.objects.get(pk=pk)
			delete_zrecipient.delete()
			return redirect('zakat_recipients')
		except:
			pass
	else:
		messages.warning(request,'Only admin user can perform this action')
		return redirect('zakat_recipients')

#**** Retrive archive data *******
def recipients_23(request):
	
	try:
		recipients_list = RecipientsArchive.objects.filter(zakat_year='2023').order_by('donation_date')
		# print(f'list: {recipients_list}')
	except RecipientsArchive.DoesNotExist:
		# text_message = 'Recipients do not exist in the year 2023.'
		pass
	context={
		'recipients_list':recipients_list,
		# 'text_message':'Recipients do not exist in the year 2023.',
	}
	return render(request,'zakat/recipients_year2023.html',context)

def recipients_24(request):
	try:
		recipients_list = RecipientsArchive.objects.filter(zakat_year='2024').order_by('donation_date')
		# print(f'list: {recipients_list}')
	except RecipientsArchive.DoesNotExist:
		message.error(request,'Recipients do not exist in the year 2024.')
	
	context={
		'recipients_list':recipients_list,
	}
	return render(request,'zakat/recipients_year2024.html',context)