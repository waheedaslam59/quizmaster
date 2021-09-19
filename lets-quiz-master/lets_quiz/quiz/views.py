# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from django.core.exceptions import ObjectDoesNotExist
# from django.http import Http404
# from django.views.generic import TemplateView
# from .models import QuizProfile, Question, AttemptedQuestion, Quizs
# from .forms import UserLoginForm, RegistrationForm
#
#
# def home(request):
#     quiz_name = Quizs.objects.all()
#     context = {'quiz_name':quiz_name}
#     return render(request, 'quiz/home.html', context=context)
#
#
# @login_required()
# def user_home(request):
#     context = {}
#     return render(request, 'quiz/user_home.html', context=context)
#
#
# def leaderboard(request):
#
#     top_quiz_profiles = QuizProfile.objects.order_by('-total_score')[:500]
#     total_count = top_quiz_profiles.count()
#     context = {
#         'top_quiz_profiles': top_quiz_profiles,
#         'total_count': total_count,
#     }
#     return render(request, 'quiz/leaderboard.html', context=context)
#
# #
# #
# # class play(TemplateView):
#
#     # def get(self, request, *args, **kwargs):
#     #     pkid = kwargs.get('id')
#     #     ques = Question.objects.filter(quiz_name=pkid)
#     #     return render(request, 'quiz/play.html', {'ques': ques})
# @login_required()
# def play(request, *args,**kwargs):
#     pkid = kwargs['id']
#     quiz_profile, created = QuizProfile.objects.get_or_create(user=request.user)
#
#     if request.method == 'POST':
#         question_pk = request.POST.get('question_pk')
#
#         attempted_question = quiz_profile.attempts.select_related('question').get(question__pk=question_pk)
#
#         choice_pk = request.POST.get('choice_pk')
#
#         try:
#             selected_choice = attempted_question.question.choices.get(pk=choice_pk)
#         except ObjectDoesNotExist:
#             raise Http404
#
#         quiz_profile.evaluate_attempt(attempted_question, selected_choice)
#
#         return redirect(attempted_question)
#
#     else:
#         question = quiz_profile.get_new_question()
#         if question is not None:
#             quiz_profile.create_attempt(question)
#
#         context = {
#             'question': question,
#         }
#
#         return render(request, 'quiz/play.html', context=context)
#     #return render(request, 'quiz/play.html', {'ques': ques})
#
#
# @login_required()
# def submission_result(request, attempted_question_pk):
#     attempted_question = get_object_or_404(AttemptedQuestion, pk=attempted_question_pk)
#     context = {
#         'attempted_question': attempted_question,
#     }
#
#     return render(request, 'quiz/submission_result.html', context=context)
#
#
# def login_view(request):
#     title = "Login"
#     form = UserLoginForm(request.POST or None)
#     if form.is_valid():
#         username = form.cleaned_data.get("username")
#         password = form.cleaned_data.get("password")
#         user = authenticate(username=username, password=password)
#         login(request, user)
#         return redirect('/user-home')
#     return render(request, 'quiz/login.html', {"form": form, "title": title})
#
#
# def register(request):
#     title = "Create account"
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/login')
#     else:
#         form = RegistrationForm()
#
#     context = {'form': form, 'title': title}
#     return render(request, 'quiz/registration.html', context=context)
#
#
# def logout_view(request):
#     logout(request)
#     return redirect('/')
#
#
# def error_404(request):
#     data = {}
#     return render(request, 'quiz/error_404.html', data)
#
#
# def error_500(request):
#     data = {}
#     return render(request, 'quiz/error_500.html', data)

from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from .forms import *
from .models import *
from django.http import HttpResponse

# Create your views here.


def startquiz(request, **kwargs):
    pkid = kwargs['id']
    if request.method == 'POST':
        questions = QuesModel.objects.filter(quiz_name=pkid)
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for q in questions:
            total += 1
            print(request.POST.get(q.question))
            print(q.ans)
            if q.ans == request.POST.get(q.question):
                score += 1
                correct += 1
            else:
                wrong += 1
        percent = score / (total) * 100
        context = {
            'score': score,
            'time': request.POST.get('timer'),
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total
        }
        return render(request, 'quiz/result.html', context)
    else:
        questions = QuesModel.objects.filter(quiz_name=pkid)

        context = {
            'questions': questions,
        }
        return render(request, 'quiz/startquiz.html', context)


def home(request):
    quizz = Quizs.objects.all()

    return render(request, 'quiz/home.html', {'quizz': quizz})


# def addQuestion(request):
#     if request.user.is_staff:
#         form = addQuestionform()
#         if request.method == 'POST':
#             form = addQuestionform(request.POST)
#             if form.is_valid():
#                 form.save()
#                 return redirect('/')
#         context = {'form' : form}
#         return render(request, 'Quiz/addQuestion.html', context)
#     else:
#         return redirect('home')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form=createuserform()
        if request.method=='POST':
            form=createuserform(request.POST)
            if form.is_valid() :
                user=form.save()
                return redirect('login')
        context={
            'form':form,
        }
        return render(request,'quiz/register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
       context={}
       return render(request,'quiz/login.html',context)

def logoutPage(request):
    logout(request)
    return redirect('/')

