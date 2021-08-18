# Generated by Django 3.2.5 on 2021-07-27 16:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='newsandupdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])),
                ('newstext', models.TextField()),
                ('newsdate', models.DateField()),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
