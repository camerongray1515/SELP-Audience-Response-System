from django.shortcuts import render, render_to_response
from main.decorators import user_is_tutor
from django.template import RequestContext
from django.http import HttpResponseRedirect
from main.models import Tutor_assignment, Tutor
from django.views.decorators.csrf import csrf_exempt

@user_is_tutor
def welcome(request):
    # request.session['course_id'] = 2
    return render_to_response('welcome.html', context_instance=RequestContext(request))

@csrf_exempt
@user_is_tutor
def select_course(request):
    course_id = int(request.POST['course'])

    # We first must check if the tutor is actually assigned to this course
    tutor = Tutor.objects.get(user=request.user)
    assignments = Tutor_assignment.objects.filter(tutor=tutor, course_id=course_id)

    # Could throw a pretty error here but in this should never happen in normal use of
    # the application
    if len(assignments) == 0:
        return HttpResponseRedirect('/tutor/')

    # We have verified that the tutor is assigned to the course
    # so we can set the session variable
    request.session['course_id'] = course_id
    return HttpResponseRedirect('/tutor/')