#this file 

from django.shortcuts import render
from django.http import HttpResponse
from .models import Exam,Question ,Answer,User

# Create your views here.
def create_exam(request):
    if request.method == 'GET':
        return render(request,'exams/createExam.html')
    elif request.method == 'POST':

        title = request.POST['title']
        desc =request.POST['desc']
        premium =request.POST['premium']
        deff =request.POST['deff']   
        examData = [title,desc,premium,deff] 
        is_prem = False
        if premium == "True":
            is_prem = True
        exam = Exam.objects.create(title=title,description=desc,deff=deff,is_premium=is_prem)
        exam.save()               
        return HttpResponse(
        exam
        )
    return 'aaa'
    
    
