# Generated by Django 5.1 on 2024-10-11 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autenticateapp', '0003_appointmentmodel_patientmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientmodel',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='patientmodel',
            name='p_pno',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
