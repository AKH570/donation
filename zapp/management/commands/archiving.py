from django.core.management.base import BaseCommand
from django.utils import timezone
from zapp.models import RecipientsArchive,ZakatRecipients

class Command(BaseCommand):
	help = 'Archive old data'

	def handle(self,*args,**kwargs):
		# Set a date threshold for archiving, e.g., records older than 1year
		# archive_threshold = timezone.now() - timezone.timedelta(days=7)
		# archive_threshold = timezone.now() - timezone.timedelta(days=21) #archive will started from last day
		# self.stdout.write(f'Archiving records older than: {archive_threshold}')
		# print(f'archive day: {archive_threshold}')

		# Get records that meet the criteria (e.g., older than 1 year and not archived)

		# shift_to_archive = ZakatRecipients.objects.filter(created_at__lt=archive_threshold,is_archived=False,zakat_year=2024)
		shift_to_archive = ZakatRecipients.objects.filter(is_archived=False,zakat_year=2024)
		print(f'archive data: {shift_to_archive}')
		for record in shift_to_archive:
				RecipientsArchive.objects.create(
					recipients_name=record.recipients_name,
					recipients_address = record.recipients_address,
					zakat_money = record.zakat_money,
					recipients_mobile = record.recipients_mobile,
					# donor_name = record.donor_name,
					remarks = record.remarks,
					recipients_category = record.recipients_category,
					zakat_year = record.zakat_year,
					donation_date =record.donation_date,
					archive_date = record.created_at
				)
				record.is_archived=True
				record.save()
			# record.delete()  # Remove from original model
			# print(f'record{[record]}')
		self.stdout.write(self.style.SUCCESS(f'Successfully archived {shift_to_archive.count()} records'))