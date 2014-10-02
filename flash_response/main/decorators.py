from django.http import HttpResponseRedirect

from main.models import Tutor, Student

def user_is_tutor(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        tutor = len(Tutor.objects.filter(user=request.user.id))

        if tutor:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/login/tutor/')
    return _wrapped_view_func

def user_is_student(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        student = len(Student.objects.filter(user=request.user.id))

        if student:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/login/student/')
    return _wrapped_view_func