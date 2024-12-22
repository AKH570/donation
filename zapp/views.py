from django.shortcuts import render,get_object_or_404,redirect
from zapp.models import Donors,DonateInfo,ZakatRecipients
from zapp.forms import DonateInfoForm,DonorsNameForm,ZakatRecipientsForm
from django.contrib import messages
from django.db.models import Sum
from django.core.exceptions import ObjectDoesNotExist


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
	
	total_donate_amount = 0
	for i in donate_info:
		total_donate_amount += i.donate_amt

	context = {
		'dname':name,
		'donate_info':donate_info,
		'donors_info':donors_info,
		'total_donate_amount':total_donate_amount
	}
	return render(request,'zakat/zdonors.html',context) # old:zcontributors.html

def Donation(request,pk):
	name = get_object_or_404(Donors,id=pk)
	print(f'name:{name}')
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

	context={
		'dinfo_form':d_info_form,
		'donor_name':donor_name_form
	}

	return render(request,'zakat/donatemoney.html',context)

def UpdateDonation(request,pk):
	get_donation = get_object_or_404(DonateInfo,pk=pk)
	try:
		get_donor = Donors.objects.get(name=get_donation)
	except Donors.DoesNotExist:
		messages.error(request,'Donor is not exist')
		return redirect('donors')

	if request.method == 'POST':
		donation_form = DonateInfoForm(request.POST,instance=get_donation)
		if donation_form.is_valid():
			donation_form.save()
			messages.success(request,'Donation have been updated successfully')
			return redirect('donors')
		else:
			print(donation_form.errors)
			
	else:
		donation_form = DonateInfoForm(instance=get_donation)
		donor_form = DonorsNameForm(instance=get_donor)

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
			zRecipients.recipients_mobile = zakat_form.cleaned_data['recipients_mobile']
			zRecipients.zakat_money = zakat_form.cleaned_data['zakat_money']
			zRecipients.recipients_category = request.POST.get('recipients_category')
			zRecipients.remarks = zakat_form.cleaned_data['remarks']
			zRecipients.zakat_date = zakat_form.cleaned_data['zakat_date']

			zRecipients.save()
			messages.success(request,'Recipients name added successfully')
			return redirect('add_zrecipient')
		else:
			print(zakat_form.errors)

	else:
		zakat_form = ZakatRecipientsForm()
	context={
		'zakat_form':zakat_form
	}
	return render(request,'zakat/add_zakat_recipients.html',context)

# To show recipients list in template
def ZakatRecipientsName(request):
	try:
		recipients_list = ZakatRecipients.objects.all().order_by('created_at')
		print(f'recipints name:{recipients_list}')
	except ZakatRecipients.DoesNotExist:
		messages.error(request,'Recipients are not added')
		return redirect('add_zrecipient')

	context={
		'recipients_list':recipients_list
	}
	return render(request,'zakat/zakat_recipients.html',context)

def EditZakatRecipients(request,pk):
	get_zakat_recipient_name = get_object_or_404(ZakatRecipients,pk=pk)
	
	if request.method=='POST':
		zakat_form = ZakatRecipientsForm(request.POST,instance=get_zakat_recipient_name)
		if zakat_form.is_valid():
			zakat_form.save()
			messages.success(request,'Recipients updated successfully')
			return redirect('zakat_recipients')
		else:
			print(zakat_form.errors)
	else:
		zakat_form = ZakatRecipientsForm(instance=get_zakat_recipient_name)
	context={
		'zakat_form':zakat_form
	}	
	return render(request,'zakat/update_zakat_recipt.html',context)

def Zyear23(request):
	return render(request,'zakat/zakatyear2023.html')