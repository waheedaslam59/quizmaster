from django.contrib.admin import register
from datetime import datetime, timedelta
from django.utils import timezone
import mimetypes
from django import template
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.template.context_processors import csrf
from .decorators import login_excluded
from .forms import SignUpForm, UserLoginForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import newsandupdate, ComingEvents, City, Programs, StudentsToped, Queries, Admission, Blogs, Reviews, Institutions, BooksCategory, FreeBooks
from .forms import CommentForm
from django.http import HttpResponseRedirect, Http404, HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
import os
from django.core.paginator import Paginator
from django.core.serializers import serialize
now = timezone.now()


def index(request):
    if request.method == "POST":
        city = request.POST.get('cities')
        inst = request.POST.get('institutes')
        pro = request.POST.get('program')
        cities = City.objects.all()
        return render(request, "eduskills/course_detail.html", {'cities': cities, 'city': city,'inst': inst, 'pro': pro})
    else:
        topedstudents = StudentsToped.objects.all()
        newblogs = Blogs.objects.all()
        featuredbooks = FreeBooks.objects.filter(featured=True)
        newsupdate = newsandupdate.objects.all()
        cities = City.objects.all()
        newevents = ComingEvents.objects.filter(From_DateTime__gt=now.date()).order_by('-From_DateTime')
        return render(request, "eduskills/index.html", {'cities': cities, 'newevents': newevents, 'newblogs': newblogs,'featuredbooks': featuredbooks, 'topedstudents': topedstudents, 'newsupdate': newsupdate})


def news(request, *args, **kwargs):
    pkid =kwargs.get('id')
    newss = newsandupdate.objects.filter(id=pkid)
    newsupdate = newsandupdate.objects.all()
    post = get_object_or_404(newsandupdate, id=kwargs.get('id'))
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()

    else:
        comment_form = CommentForm()
    return render(request, "eduskills/news.html", {'newss': newss, 'newsupdate': newsupdate,'post': post,
                                                   'comments': comments,
                                                   'new_comment': new_comment,
                                                   'comment_form': comment_form})


def course_detail(request, **kwargs):
    # pkid = kwargs.get('ist')
    pid = kwargs.get('secondid')
    # categ = ProgramCategory.objects.filter(Category_name=pkid)
    cities = City.objects.all()
    # courses = Programs.objects.filter(program_category=pkid)
    # programs = ProgramCategory.objects.all()
    return render(request, 'eduskills/course_detail.html', {'cities':cities})


def staff_detail(request):
    response = ""
    # request should be ajax and method should be POST.
    if request.method == "POST":
        city1 = request.POST.get('cityname')
        response = Institutions.objects.filter(ins_city=city1)
        data = serialize("json", response, fields='institution_name')
        return HttpResponse(data, content_type="application/json")


def staff_detail2(request):
    response = ""
    # request should be ajax and method should be POST.
    if request.method == "POST":
        inst = request.POST.get("institutes")
        response = Programs.objects.filter(uniname=inst)
        data = serialize("json", response, fields='program_name')
        return HttpResponse(data, content_type="application/json")


def staff_detail3(request):
    response = ""
    # request should be ajax and method should be POST.
    if request.method == "POST":
        pro = request.POST.get("program")
        print(pro)
        inst = request.POST.get("institute")
        cities = request.POST.get("cities")
        response = Programs.objects.filter(id=pro)
        print(response)
        data = serialize("json", response, fields=('Duration', 'fee', 'description', 'program_name'))
        return HttpResponse(data, content_type="application/json")


def mcqspdf(request, *args, **kwargs):
    # path = kwargs['path']
    book_categ = BooksCategory.objects.get(category_name="Computer")
    computer = FreeBooks.objects.filter(Q(book_category=book_categ) & Q(Booksnotes="Notes"))
    paginator = Paginator(computer, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # programs = ProgramCategory.objects.all()
    return render(request, 'eduskills/mcqspdf.html', {'page_obj': page_obj})


def blogposts(request, *args, **kwargs):
    # path = kwargs['path']
    posts = Blogs.objects.all()
    paginator = Paginator(posts, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # programs = ProgramCategory.objects.all()
    return render(request, 'eduskills/blogs.html', {'page_obj': page_obj})


def blogdetail(request, *args, **kwargs):
    pkid = kwargs['id']
    msg=""
    counting=0
    posts = Blogs.objects.filter(id=pkid)
    allreviews = Reviews.objects.filter(Blogname=pkid)
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        feedback = request.POST.get("comment")
        bookreview = Blogs.objects.get(id=pkid)
        rev = Reviews()
        rev.Blogname = bookreview
        rev.name = name
        rev.email = email
        rev.feedback = feedback
        rev.posted_date = datetime.now()
        rev.save()
        if rev:
            msg = "review saved Successfully"
            sts = "success"
    # programs = ProgramCategory.objects.all()
    for i in allreviews:
        counting=counting+1
    return render(request, 'eduskills/blogdetail.html', {'counting': counting, 'posts': posts, 'allreviews': allreviews, 'msg': msg,})


def nineclass(request, *args, **kwargs):
    # path = kwargs['path']
    book_categ = BooksCategory.objects.get(category_name="9thclass")
    computer = FreeBooks.objects.filter(Q(book_category=book_categ) & Q(Booksnotes="PastPapers"))
    paginator = Paginator(computer, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # programs = ProgramCategory.objects.all()
    return render(request, 'eduskills/9thclass.html', {'page_obj': page_obj})


def tenclass(request, *args, **kwargs):
    # path = kwargs['path']
    book_categ = BooksCategory.objects.get(category_name="10thclass")
    computer = FreeBooks.objects.filter(Q(book_category=book_categ) & Q(Booksnotes="PastPapers"))
    paginator = Paginator(computer, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # programs = ProgramCategory.objects.all()
    return render(request, 'eduskills/10thclass.html', {'page_obj': page_obj})


def elevenclass(request, *args, **kwargs):
    # path = kwargs['path']
    book_categ = BooksCategory.objects.get(category_name="11thclass")
    computer = FreeBooks.objects.filter(Q(book_category=book_categ) & Q(Booksnotes="PastPapers"))
    paginator = Paginator(computer, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # programs = ProgramCategory.objects.all()
    return render(request, 'eduskills/11thclass.html', {'page_obj': page_obj})


def twelveclass(request, *args, **kwargs):
    # path = kwargs['path']
    book_categ = BooksCategory.objects.get(category_name="12thclass")
    computer = FreeBooks.objects.filter(Q(book_category=book_categ) & Q(Booksnotes="PastPapers"))
    paginator = Paginator(computer, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # programs = ProgramCategory.objects.all()
    return render(request, 'eduskills/12thclass.html', {'page_obj': page_obj})


def computerbooks(request, *args, **kwargs):
    # path = kwargs['path']
    book_categ = BooksCategory.objects.get(category_name="Computer")
    computer = FreeBooks.objects.filter(Q(book_category=book_categ) & Q(Booksnotes="Books"))
    paginator = Paginator(computer, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # programs = ProgramCategory.objects.all()
    return render(request, 'eduskills/computerbooks.html', {'page_obj': page_obj})


def programmingbooks(request, *args, **kwargs):
    # path = kwargs['path']
    book_categ = BooksCategory.objects.get(category_name="Programming")
    computer = FreeBooks.objects.filter(Q(book_category=book_categ) & Q(Booksnotes="Books"))
    paginator = Paginator(computer, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # programs = ProgramCategory.objects.all()
    return render(request, 'eduskills/programmingbooks.html', {'page_obj': page_obj})


def knowledgebooks(request, *args, **kwargs):
    # path = kwargs['path']
    book_categ = BooksCategory.objects.get(category_name="General Knowledge")
    computer = FreeBooks.objects.filter(Q(book_category=book_categ) & Q(Booksnotes="Books"))
    paginator = Paginator(computer, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # programs = ProgramCategory.objects.all()
    return render(request, 'eduskills/knowledgebooks.html', {'page_obj': page_obj})


def studybooks(request, *args, **kwargs):
    # path = kwargs['path']
    book_categ = BooksCategory.objects.get(category_name="Study Related")
    computer = FreeBooks.objects.filter(Q(book_category=book_categ) & Q(Booksnotes="Books"))
    paginator = Paginator(computer, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # programs = ProgramCategory.objects.all()
    return render(request, 'eduskills/studybooks.html', {'page_obj': page_obj})


def Englishnotes(request, *args, **kwargs):
    # path = kwargs['path']
    book_categ = BooksCategory.objects.get(category_name="English")
    computer = FreeBooks.objects.filter(Q(book_category=book_categ) & Q(Booksnotes="Notes"))
    paginator = Paginator(computer, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # programs = ProgramCategory.objects.all()
    return render(request, 'eduskills/englishnotes.html', {'page_obj': page_obj})


def knowledgenotes(request, *args, **kwargs):
    # path = kwargs['path']
    book_categ = BooksCategory.objects.get(category_name="General Knowledge")
    computer = FreeBooks.objects.filter(Q(book_category=book_categ) & Q(Booksnotes="Notes"))
    paginator = Paginator(computer, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # programs = ProgramCategory.objects.all()
    return render(request, 'eduskills/knowledgenotes.html', {'page_obj': page_obj})


def Urdu(request, *args, **kwargs):
    # path = kwargs['path']
    book_categ = BooksCategory.objects.get(category_name="Urdu")
    computer = FreeBooks.objects.filter(Q(book_category=book_categ) & Q(Booksnotes="Notes"))
    paginator = Paginator(computer, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # programs = ProgramCategory.objects.all()
    return render(request, 'eduskills/urdu.html', {'page_obj': page_obj})


def download_file(request, **kwargs):

        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filename = kwargs.get('filename')
        # Define the full file path
        filepath = BASE_DIR + '/edustatic/pdf/' + filename
        # Open the file for reading content
        path = open(filepath, 'r', newline='', encoding="cp437", errors='ignore')

        # Set the mime type
        mime_type, _ = mimetypes.guess_type(filepath)
        # Set the return value of the HttpResponse
        response = HttpResponse(path, content_type=mime_type)
        # Set the HTTP header for sending to browser
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        # Return the response value
        return response


def singlebook(request, *args, **kwargs):
    pkid = kwargs['pk']
    fetchbook = FreeBooks.objects.filter(id=pkid)
    # programs = ProgramCategory.objects.all()
    return render(request, 'eduskills/singlebook.html', {'fetchbook': fetchbook})


@login_excluded("/")
def signup(request):
    msg = ""
    sts = ""
    try:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save(commit=True)
                # auth.authenticate(email=form.cleaned_data.get('email'),
                # password=form.cleaned_data.get('password1'))
                # auth.login(request, user)
                # cart = Cart()
                # cart.user = user
                msg = "User Registered Successfully"
                sts = "success"
        else:
            form = SignUpForm()
    except Exception:
        msg = "Email Already Registered! Please go to login"
        sts = "danger"
    return render(request, 'eduskills/signup.html', {'form': form, 'msg': msg, 'sts': sts})


@login_excluded("/")
def login(request):
    # redirect_to = request.get('next')
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = auth.authenticate(username=email, password=password)
            if user:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in.")

                success_url = request.POST.get('previous_page')
                return redirect(success_url)
            else:
                form.add_error(None, "Your email or password was not recognised. Please try again.")
    else:
        form = UserLoginForm()

    args = {'form': form}
    args.update(csrf(request))
    return render(request, 'eduskills/login.html', args)


@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out. See you soon!')
    return redirect('/')


def AboutUs(request):
    # programs = ProgramCategory.objects.all()
    return render(request,'eduskills/aboutus.html')


def Event(request):
    # programs = ProgramCategory.objects.all()
    newevents = ComingEvents.objects.filter(From_DateTime__gt=now.date()).order_by('-From_DateTime')
    return render(request,'eduskills/eventcalender.html', {'newevents': newevents})


def EventDetail(request, *args, **kwargs):
    pkid = kwargs.get('id')
    # programs = ProgramCategory.objects.all()
    newevents = ComingEvents.objects.filter(id=pkid)
    return render(request, 'eduskills/eventdetail.html', {'newevents': newevents})


def ContactUs(request):
    msg = ""
    sts = ""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if email or subject or message:
            try:
                record = Queries()
                record.name = name
                record.email = email
                record.subject = subject
                record.message = message
                record.save()
                if record:
                    msg = "Query saved Successfully. We will reply your email immediately"
                    sts = "success"

                    send_mail(
                        subject,
                        message,
                        email,
                        ['waheedaslam59@gmail.com'],
                        fail_silently=False,
                    )
                else:
                    msg = "Somethong went wrong"
                    sts = 'danger'
            except BadHeaderError:
                return HttpResponse('Invalstid header found.')
        else:
            return HttpResponse('Make sure all fields are entered')
    # programs = ProgramCategory.objects.all()
    return render(request,'eduskills/contactus.html', {'msg': msg, 'sts': sts})


def institutes(request):
    schools = Institutions.objects.all()
    return render(request, 'eduskills/initutes.html', {'schools': schools})


def latestadmissions(request):
    admissions = ""
    msg = ""
    if request.method == "POST":
        cityname = request.POST.get("cityname")
        institute = request.POST.get("institutes")
        admissions = Admission.objects.filter(Q(university=institute) & Q(in_progress=True))
        if admissions:
            print("admissions open")
        else:
            msg = "there is no admission"
    cities = City.objects.all()
    ad = Admission.objects.filter(in_progress=True).order_by('last_date')
    return render(request, 'eduskills/latestadmissions.html', {'cities': cities, 'ad': ad, 'admissions': admissions, 'msg': msg})


def admissiondetail(request, *args, **kwargs):
    pkid = kwargs['id']
    adm = Admission.objects.filter(university=pkid)
    return render(request, 'eduskills/admissiondetail.html', {'adm': adm})
