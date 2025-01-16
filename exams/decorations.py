from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

def teacher_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == 'teacher':
            return view_func(request, *args, **kwargs)
        # If user is not authenticated or not a teacher, redirect to the unauthorized page
        return redirect('/exams/login/teacher/')  # Replace with your unauthorized page
    return _wrapped_view