#this is file for our Database schema, which is the structure of data in the app

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = [('admin', 'Admin'), ('teacher', 'Teacher'), ('student', 'Student')]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)


class Exam(models.Model):
    difficulty = {
        'e':'easy',
        'm':'medium',
        'h':'hard'
    }
    title = models.CharField(max_length=30)
    description = models.TextField()
    deff = models.CharField(choices=difficulty,max_length=10)
    is_premium = models.BooleanField(default=False)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,limit_choices_to={'role':'teacher'},default=1)

    def __str__(self):
        return self.title
class Question(models.Model):
    question_types= [('MC','multiple choice'),
        ('TF','True/False'),
        ('SA','Short answer')]
    
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE,related_name='questions')
    question_type = models.CharField(choices=question_types, max_length=50)
    question_text = models.TextField()

class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE,related_name='answer')
    correct_answer = models.TextField()

class Submition(models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE,limit_choices_to={'role':'student'})
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    submission_data = models.JSONField()  # Submitted answers as JSON
    grade = models.IntegerField(default=0)

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)  # Paid or not




