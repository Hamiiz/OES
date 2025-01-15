# this file manages urls within the exams app
from django.urls import path
from . import views

urlpatterns = [
    
]

# urlpatterns = [
#     path('exam/create/', views.create_exam, name='create_exam'),
#     path('exam/<int:id>/', views.view_exam, name='view_exam'),
#     path('exam/<int:id>/submit/', views.submit_exam, name='submit_exam'),
#     path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
#     path('payment/', views.payment_page, name='payment_page'),
# ]
