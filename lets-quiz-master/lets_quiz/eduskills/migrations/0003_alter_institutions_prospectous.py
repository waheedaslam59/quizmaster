# Generated by Django 3.2.7 on 2021-10-03 13:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduskills', '0002_rename_uni_name_programs_uniname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institutions',
            name='prospectous',
            field=models.FileField(upload_to='edustatic/pdf/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf'])]),
        ),
    ]
