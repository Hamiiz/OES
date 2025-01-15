from django.contrib import admin
from .models import User, Payment,Question,Answer,Submition
admin.site.register(User)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Submition)
admin.site.register(Payment)


# Register your models here.
