# Generated by Django 3.2.7 on 2021-09-28 16:09

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=1000)),
                ('published_date', models.DateField(auto_now_add=True)),
                ('text', models.TextField(default='')),
                ('blog_image', models.ImageField(upload_to='edustatic/images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BooksCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ComingEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=700)),
                ('From_DateTime', models.DateTimeField()),
                ('To_DateTime', models.DateTimeField()),
                ('body', models.TextField()),
                ('Host_name', models.CharField(max_length=900)),
                ('Contact_info', models.IntegerField()),
                ('Host_Email', models.EmailField(max_length=254)),
                ('uploaded_date', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(max_length=700)),
                ('event_image', models.ImageField(upload_to='edustatic/images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])),
            ],
        ),
        migrations.CreateModel(
            name='Institutions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_name', models.CharField(max_length=500)),
                ('prospectous', models.FileField(upload_to='edustatic/images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['xlsx', 'xls', 'doc', 'docx', 'pdf'])])),
                ('image', models.ImageField(upload_to='edustatic/images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])),
                ('ins_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eduskills.city')),
            ],
        ),
        migrations.CreateModel(
            name='newsandupdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='edustatic/images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])),
                ('newstext', models.TextField()),
                ('newsdate', models.DateField()),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Queries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(default='', max_length=500)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='StudentsToped',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=500)),
                ('student_class', models.CharField(max_length=600)),
                ('studied_in', models.CharField(max_length=800)),
                ('board_name', models.CharField(max_length=800)),
                ('toped_year', models.IntegerField()),
                ('student_image', models.ImageField(upload_to='edustatic/images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('email', models.EmailField(default='', max_length=254)),
                ('feedback', models.TextField()),
                ('posted_date', models.DateTimeField()),
                ('Blogname', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='eduskills.blogs')),
            ],
        ),
        migrations.CreateModel(
            name='Programs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_name', models.CharField(max_length=500)),
                ('Duration', models.CharField(max_length=400)),
                ('fee', models.IntegerField()),
                ('description', models.TextField()),
                ('uni_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eduskills.institutions')),
            ],
        ),
        migrations.CreateModel(
            name='FreeBooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('Booksnotes', models.CharField(choices=[('Books', 'Books'), ('Notes', 'Notes'), ('PastPapers', 'PastPapers')], default='Books', max_length=20)),
                ('author', models.CharField(max_length=500)),
                ('isbn', models.CharField(max_length=300)),
                ('published_year', models.CharField(max_length=200)),
                ('book_description', models.TextField(default='')),
                ('book_image', models.ImageField(upload_to='edustatic/images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])),
                ('bookpdf', models.FileField(upload_to='edustatic/pdf/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])])),
                ('uploaded_date', models.DateTimeField(auto_now_add=True)),
                ('featured', models.BooleanField(default=False)),
                ('book_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eduskills.bookscategory')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='eduskills.newsandupdate')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_image', models.ImageField(upload_to='edustatic/images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])),
                ('description', models.TextField()),
                ('last_date', models.DateField()),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eduskills.programs')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eduskills.institutions')),
            ],
        ),
    ]
