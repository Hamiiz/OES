from django.contrib import admin
from .models import User, Payment,Question,Answer,Submition,Exam
admin.site.register(User)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Submition)
admin.site.register(Payment)
admin.site.register(Exam)


# Register your models here.
