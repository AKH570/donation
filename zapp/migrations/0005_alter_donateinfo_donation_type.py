# Generated by Django 5.1.4 on 2024-12-19 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zapp', '0004_donateinfo_donation_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donateinfo',
            name='donation_type',
            field=models.CharField(choices=[('donation', 'Donation'), ('zakat', 'Zakat'), ('other', 'Other_purpose')], default='', max_length=50, null=True),
        ),
    ]
