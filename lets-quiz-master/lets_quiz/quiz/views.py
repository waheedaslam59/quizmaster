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

