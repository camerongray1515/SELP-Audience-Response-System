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

# If a course has not been seleceted in the tutor area, redirect to the tutor home
# page which will show a message telling the user to select a course
def tutor_course_is_selected(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        if 'course_id' in request.session:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/tutor/')
    return _wrapped_view_func