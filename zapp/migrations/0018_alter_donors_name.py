# Generated by Django 5.1.4 on 2025-01-04 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zapp', '0017_remove_zakatrecipients_donor_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donors',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
