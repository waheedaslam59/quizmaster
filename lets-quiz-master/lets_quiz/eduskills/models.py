from django.db import models
from django.core.validators import FileExtensionValidator
import os
import datetime
from django.contrib.auth.models import User
# Create your models here.


class newsandupdate(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='edustatic/images/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    newstext = models.TextField()
    newsdate = models.DateField()
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(newsandupdate, on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


class City(models.Model):
    city_name = models.CharField(max_length=500)

    def __str__(self):
        return self.city_name


class Institutions(models.Model):
    institution_name = models.CharField(max_length=500)
    ins_city = models.ForeignKey(City, on_delete=models.CASCADE)
    prospectous = models.FileField(upload_to='edustatic/pdf/', validators=[FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf'])])
    image = models.ImageField(upload_to='edustatic/images/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])

    def __str__(self):
        return self.institution_name


# class StudentLevel(models.Model):
#     level = models.CharField(max_length=500)
#     uni = models.ForeignKey(Institutions, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.level
#
#
# class ProgramCategory(models.Model):
#     Category_name = models.CharField(max_length=500)
#     level_of_student = models.ForeignKey(StudentLevel, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.Category_name


class Programs(models.Model):
    uniname = models.ForeignKey(Institutions, on_delete=models.CASCADE)
    # program_category = models.ForeignKey(ProgramCategory, on_delete=models.CASCADE)
    program_name = models.CharField(max_length=500)
    Duration = models.CharField(max_length=400)
    fee = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.program_name


class Admission(models.Model):
    university = models.ForeignKey(Institutions, on_delete=models.CASCADE)
    course = models.ForeignKey(Programs, on_delete=models.CASCADE)
    ad_image = models.ImageField(upload_to='edustatic/images/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    description = models.TextField()
    last_date = models.DateField()
    upload_date = models.DateTimeField(auto_now_add=True)
    in_progress = models.BooleanField(default=True)

    def __str__(self):
        return self.university.institution_name

    def save(self, *args, **kw):

        if self.last_date < datetime.datetime.now().date():
            self.in_progress = False
        super(Admission, self).save(*args, **kw)


class BooksCategory(models.Model):
    category_name = models.CharField(max_length=500)

    def __str__(self):
        return self.category_name


Book_Choices = (
    ('Books', "Books"),
    ('Notes', 'Notes'),
    ('PastPapers', 'PastPapers'),
)


class FreeBooks(models.Model):
    book_category = models.ForeignKey(BooksCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    Booksnotes = models.CharField(max_length=20, choices=Book_Choices, default='Books')
    author = models.CharField(max_length=500)
    isbn = models.CharField(max_length=300)
    published_year = models.CharField(max_length=200)
    book_description = models.TextField(default='')
    book_image = models.ImageField(upload_to='edustatic/images/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    bookpdf = models.FileField(upload_to='edustatic/pdf/', validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    uploaded_date = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)

    def filename(self):
        return os.path.basename(self.bookpdf.name)

    def __str__(self):
        return self.title


class Queries(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    subject = models.CharField(max_length=500, default='')
    message = models.TextField()

    def __str__(self):
        return self.subject


class Blogs(models.Model):
    title = models.CharField(max_length=1000, default="")
    published_date = models.DateField(auto_now_add=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(default="")
    blog_image = models.ImageField(upload_to='edustatic/images/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])

    def __str__(self):
        return self.title


class Reviews(models.Model):
    Blogname = models.ForeignKey(Blogs, on_delete=models.CASCADE, default="")
    name = models.CharField(max_length=200, default="")
    email = models.EmailField(default="")
    feedback = models.TextField()
    posted_date = models.DateTimeField()

    def __str__(self):
        return self.name


class StudentsToped(models.Model):
    student_name = models.CharField(max_length=500)
    student_class = models.CharField(max_length=600)
    studied_in = models.CharField(max_length=800)
    board_name = models.CharField(max_length=800)
    toped_year = models.IntegerField()
    student_image = models.ImageField(upload_to='edustatic/images/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    description = models.TextField()

    def __str__(self):
        return '{} Toped by {}'.format(self.student_name, self.toped_year)


class ComingEvents(models.Model):
    title = models.CharField(max_length=700)
    From_DateTime = models.DateTimeField()
    To_DateTime = models.DateTimeField()
    body = models.TextField()
    Host_name = models.CharField(max_length=900)
    Contact_info = models.IntegerField()
    Host_Email = models.EmailField()
    uploaded_date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=700)
    event_image = models.ImageField(upload_to='edustatic/images/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])

    def __str__(self):
        return '{} Toped by {}'.format(self.title, self.From_DateTime)