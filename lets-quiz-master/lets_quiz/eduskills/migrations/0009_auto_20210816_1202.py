# Generated by Django 3.2.5 on 2021-08-16 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduskills', '0008_freebooks_booksnotes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='queries',
            name='phone_no',
        ),
        migrations.AddField(
            model_name='queries',
            name='subject',
            field=models.CharField(default='', max_length=500),
        ),
    ]