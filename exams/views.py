#this file 

from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Exam,Question ,Answer,User
from django.contrib.auth import authenticate,login,logout
from .decorations import teacher_required




# Create your views here.
def auth(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('create_exam')
        else:
            return HttpResponse('Incorrect user')
    
    else:
        if request.path == 'exams/login/teacher':
            return render(request,'exams/login.html')
        return render(request,'exams/login.html')

def Logout(request):
    
    logout(request)
    return redirect('login')

@teacher_required 
def create_exam(request):
    if request.method == 'GET':
        
        return render(request,'exams/createExam.html')
    elif request.method == 'POST':
        title = request.POST['title']
        desc =request.POST['desc']
        premium =request.POST['premium']
        deff =request.POST['deff']   
        is_prem = False
        if premium == "True":
            is_prem = True
        exam = Exam.objects.create(title=title,description=desc,deff=deff,is_premium=is_prem)
        exam.save()               
        return HttpResponse(
        exam
        )

def view_exam(request,id):
    if request.method == 'GET':
       try:

            exam = Exam.objects.get(pk=id)
            return HttpResponse(exam)
       except Question.DoesNotExist:
           raise Http404('This exam Does not exist')
       

           
      

    
    
