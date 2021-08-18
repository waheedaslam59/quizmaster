# Generated by Django 3.2.5 on 2021-08-06 18:45

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eduskills', '0004_auto_20210730_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='BooksCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='FreeBooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('author', models.CharField(max_length=500)),
                ('isbn', models.CharField(max_length=300)),
                ('published_year', models.CharField(max_length=200)),
                ('book_image', models.ImageField(upload_to='edustatic/images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])),
                ('bookpdf', models.FileField(upload_to='edustatic/pdf/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])])),
                ('uploaded_date', models.DateTimeField(auto_now_add=True)),
                ('book_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eduskills.bookscategory')),
            ],
        ),
    ]