# Generated by Django 5.1.4 on 2024-12-21 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zapp', '0011_alter_zakatrecipients_donor_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zakatrecipients',
            name='recipients_category',
            field=models.CharField(choices=[('general', 'GENERAL'), ('special', 'SPECIAL')], default='general', max_length=50),
        ),
    ]